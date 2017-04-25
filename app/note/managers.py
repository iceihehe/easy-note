# -*- coding: utf-8 -*-

from bson import ObjectId

from flask_login import current_user

from ..models import Notebook, Note
from ..constants import Code


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


class NoteManager(object):

    @classmethod
    def add_note(cls, notebook_id, title, **kwargs):
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
        ).save()
        notebook.update(inc__number_notes=1)

        return note

    @classmethod
    def old_get_notes(cls):
        """获取笔记本和笔记"""

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
        ])
        result = list(result)
        result_map = {}

        def _parent(i):
            i['sub'] = []
            result_map[str(i['_id'])] = i

        list(map(_parent, result))
        need_delete = {}

        def _sub(i):
            key = i[0]
            value = i[1]

            if value.get('parent_notebook_id'):
                result_map[str(value['parent_notebook_id'])]['sub'].append(value)
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

    @classmethod
    def get_notes(cls, notebook_id):
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
