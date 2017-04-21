# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_login import login_required

from .parsers import add_notebook_parser, update_notebook_parser, delete_notebook_parser
from .managers import NotebookManager
from ..functions import make_response


class AddNotebookResource(Resource):

    @login_required
    def post(self):
        """创建笔记本"""

        req = add_notebook_parser.parse_args(strict=True)
        title = req['title']
        parent_notebook_id = req['parent_notebook_id']

        result = NotebookManager.add_notebook(title, parent_notebook_id)
        if isinstance(result, int):
            return make_response(code=result)

        return make_response({
            'notebook_id': result.id,
        })
