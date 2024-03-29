# -*- coding: utf-8 -*-

from flask_restful import Api
from flask import Blueprint

from .restfuls import (
        AddNotebookResource, AddNoteResource, ListNotesResource,
        UpdateNotebookResource, DeleteNotebookResource, UpdateNoteResource,
        DeleteNoteResource, GetNoteResource, ListNotebooksResource,
        SearchResource
    )


note = Blueprint('note', __name__)
note_wrap = Api(note)

note_wrap.add_resource(AddNotebookResource, '/api/notebook/add_notebook/')
note_wrap.add_resource(UpdateNotebookResource, '/api/notebook/update_notebook/')
note_wrap.add_resource(DeleteNotebookResource, '/api/notebook/delete_notebook/')

note_wrap.add_resource(ListNotesResource, '/api/note/list_notes/')
note_wrap.add_resource(AddNoteResource, '/api/notebook/add_note/')
note_wrap.add_resource(UpdateNoteResource, '/api/note/update_note/')
note_wrap.add_resource(DeleteNoteResource, '/api/note/delete_note/')
note_wrap.add_resource(GetNoteResource, '/api/note/get_note/')
note_wrap.add_resource(ListNotebooksResource, '/api/notebook/list_notebooks/')
note_wrap.add_resource(SearchResource, '/api/note/search/')
