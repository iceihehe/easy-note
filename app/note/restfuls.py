# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_login import login_required, current_user

from .parsers import (
        add_notebook_parser, add_note_parser, update_notebook_parser,
        delete_notebook_parser, list_notes_parser, update_note_parser,
        delete_note_parser, get_note_parser
    )
from .managers import NotebookManager, NoteManager
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


class AddNoteResource(Resource):

    @login_required
    def post(self):
        """创建笔记"""

        req = add_note_parser.parse_args()
        title = req['title']
        notebook_id = req['notebook_id']
        desc = req['desc']
        tags = req['tags']

        result = NoteManager.add_note(notebook_id, title, desc, tags)

        if isinstance(result, int):
            return make_response(code=result)

        return make_response({
                'note_id': result.id,
            })


class ListNotesResource(Resource):

    @login_required
    def get(self):
        """获取某笔记本的笔记"""

        req = list_notes_parser.parse_args(strict=True)
        notebook_id = req['notebook_id']

        result = NoteManager.list_notes(notebook_id)

        if isinstance(result, int):
            return make_response(code=result)

        return make_response({'result': result})


class UpdateNotebookResource(Resource):

    @login_required
    def post(self):
        """修改笔记本"""

        req = update_notebook_parser.parse_args(strict=True)
        title = req['title']
        notebook_id = req['notebook_id']

        result = NotebookManager.update_notebook(title, notebook_id)

        return make_response(code=result)


class DeleteNotebookResource(Resource):

    @login_required
    def get(self):
        """删除笔记本"""

        req = delete_notebook_parser.parse_args(strict=True)
        notebook_id = req['notebook_id']

        result = NotebookManager.delete_notebook(notebook_id)

        return make_response(code=result)


class UpdateNoteResource(Resource):

    @login_required
    def post(self):
        """修改笔记"""

        req = update_note_parser.parse_args(strict=True)

        note_id = req['note_id']
        title = req['title']
        desc = req['desc']
        tags = req['tags']

        result = NoteManager.update_note(note_id, title, desc, tags)

        return make_response(code=result)


class DeleteNoteResource(Resource):

    @login_required
    def post(self):
        """删除笔记"""

        req = delete_note_parser.parse_args(strict=True)

        note_id = req['note_id']

        result = NoteManager.delete_note(note_id)

        return make_response(code=result)


class GetNoteResource(Resource):

    @login_required
    def get(self):
        """获取笔记"""

        req = get_note_parser.parse_args(strict=True)

        note_id = req['note_id']

        result = NoteManager.get_note(note_id, current_user)

        if isinstance(result, int):
            return make_response(code=result)

        return make_response(result)


class ListNotebooksResource(Resource):

    @login_required
    def get(self):
        """获取笔记本"""

        result = NotebookManager.list_notebooks()

        return make_response(result)
