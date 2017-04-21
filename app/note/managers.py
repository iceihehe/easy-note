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
    def get_notes(cls):
        """获取笔记本和笔记"""

        result = Notebook._get_collection().aggregate([
            {'$match': {'user_id': current_user.id}},
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
        ])

        return list(result)
