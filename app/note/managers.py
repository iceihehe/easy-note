# -*- coding: utf-8 -*-

from bson import ObjectId

from flask_login import current_user

from ..models import Notebook
from ..constants import Code


class NotebookManager(object):

    @classmethod
    def add_notebook(cls, title, parent_notebook_id):
        """添加笔记本"""

        if parent_notebook_id is not None:
            try:
                parent_notebook = Notebook.objects.get(id=parent_notebook_id)
            except:
                # TODO 日志
                return Code.NO_SUCH_PARENT_NOTEBOOK

            parent_notebook_id = ObjectId(parent_notebook_id)

        notebook = Notebook(
            title=title,
            number_notes=0,
            user_id=current_user.id,
            parent_notebook_id=parent_notebook_id,
        ).save()
        return notebook
