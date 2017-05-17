# -*- coding: utf-8 -*-

import datetime

from bson import ObjectId
from flask_login import current_user

from ..models import Notebook, Note
from ..constants import Code
from ..functions import add_history


class NotebookManager(object):

    @classmethod
    def add_notebook(cls, title, parent_notebook_id):
        """添加笔记本"""

        if parent_notebook_id is not None:
            try:
                Notebook.objects.get(id=parent_notebook_id)
            except:
                # TODO 日志
                return Code.NO_SUCH_NOTEBOOK

            parent_notebook_id = ObjectId(parent_notebook_id)

        notebook = Notebook(
            title=title,
            number_notes=0,
            user_id=current_user.id,
            parent_notebook_id=parent_notebook_id,
        ).save()
        return notebook

    @classmethod
    def update_notebook(cls, title, notebook_id):
        """修改笔记本"""

        result = Notebook.objects(id=notebook_id).update(set__title=title)

        if result == 0:
            return Code.NO_SUCH_NOTEBOOK

        return Code.SUCCESS

    @classmethod
    def delete_notebook(cls, notebook_id):
        """删除笔记本"""

        result = Notebook.objects(id=notebook_id).update(set__is_deleted=True)

        if result == 0:
            return Code.NO_SUCH_NOTEBOOK

        return Code.SUCCESS

    @classmethod
    def list_notebooks(cls):
        """获取笔记本"""

        result = Notebook._get_collection().aggregate([
            {'$match': {'user_id': current_user.id, 'is_deleted': False}},
            {
                '$lookup': {
                    'from': Note._get_collection().name,
                    'localField': '_id',
                    'foreignField': 'notebook_id',
                    'as': 'notes',
                },
            },
            {
                '$unwind': {
                    'path': '$notes',
                    'preserveNullAndEmptyArrays': True,
                },
            },
            {
                '$match': {
                    '$or': [
                        {'notes.is_deleted': False, 'notes.is_trash': False},
                        {'notes': None},
                    ],
                }
            },
            {
                '$project': {
                    '_id': 0,
                    'value': '$_id',
                    'text': '$title',
                    'parent_notebook_id': '$parent_notebook_id',
                },
            }
        ])
        result = list(result)
        result_map = {}

        def _parent(i):
            i['children'] = []
            result_map[str(i['value'])] = i

        list(map(_parent, result))
        need_delete = {}

        def _sub(i):
            key = i[0]
            value = i[1]

            if value.get('parent_notebook_id') and str(value.get('parent_notebook_id')) in result_map:
                result_map[str(value['parent_notebook_id'])]['children'].append(value)
                need_delete[key] = True

        list(map(_sub, result_map.items()))
        final = []

        def _delete(i):
            key = i[0]
            value = i[1]
            if not need_delete.get(key):
                final.append(value)

        list(map(_delete, result_map.items()))

        return final


class NoteManager(object):

    @classmethod
    def add_note(cls, notebook_id, title, desc, tags):
        """添加笔记"""

        try:
            notebook = Notebook.objects.get(id=notebook_id)
        except:
            # TODO 日志
            return Code.NO_SUCH_NOTEBOOK

        note = Note(
            title=title,
            user_id=current_user.id,
            notebook_id=notebook.id,
            desc=desc,
            tags=tags,
        ).save()
        notebook.update(inc__number_notes=1)

        return note

    @classmethod
    def list_notes(cls, notebook_id):
        """获取某笔记本的笔记"""

        try:
            Notebook.objects.get(id=notebook_id)
        except:
            # TODO 日志
            return Code.NO_SUCH_NOTEBOOK

        notes = Note.objects(notebook_id=notebook_id, is_deleted=False, is_trash=False).all()

        def _detail(note):
            res = {
                'note_id': note.id,
                'title': note.title,
                'create_time': note.create_time,
                'last_update': note.last_update,
            }
            return res

        return [_detail(i) for i in notes]

    @classmethod
    def update_note(cls, note_id, title, desc, tags):
        """修改笔记"""

        now = datetime.datetime.now()

        result = Note.objects(id=note_id).update(
            set__title=title,
            set__desc=desc,
            set__tags=tags,
            set__last_update=now, 
        )

        if result == 0:
            return Code.NO_SUCH_NOTE

        return Code.SUCCESS

    @classmethod
    def delete_note(cls, note_id):
        """删除笔记本"""

        now = datetime.datetime.now()

        try:
            note = Note.objects.get(id=note_id)
        except:
            # TODO 日志
            return Code.NO_SUCH_NOTE

        try:
            notebook = Notebook.objects.get(id=note.notebook_id)
        except:
            # TODO 日志
            return Code.NO_SUCH_NOTEBOOK

        if note.is_trash:
            note.update(set__is_deleted=True, set__last_update=now)
        else:
            note.update(set__is_trash=True, set__last_update=now)

        notebook.update(inc__number_notes=-1, set__last_update=now)

        return Code.SUCCESS

    @classmethod
    def get_note(cls, note_id, user=None):
        """获取笔记"""

        try:
            note = Note.objects.get(id=note_id)
        except:
            # TODO 日志
            return Code.NO_SUCH_NOTE

        def _detail(n):
            res = {
                'title': n.title,
                'desc': n.desc,
                'tags': n.tags,
                'note_id': n.id,
            }
            return res

        if user:
            # 记录
            add_history(note.id, note.title, note.notebook_id, user)

        return _detail(note)
