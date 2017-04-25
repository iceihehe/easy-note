# -*- coding: utf-8 -*-

from flask_restful import Api
from flask import Blueprint

from .restfuls import (AddNotebookResource, AddNoteResource, ListNotesResource,
                    UpdateNotebookResource, DeleteNotebookResource)


note = Blueprint('note', __name__)
note_wrap = Api(note)

note_wrap.add_resource(AddNotebookResource, '/api/notebook/add_notebook/')
note_wrap.add_resource(AddNoteResource, '/api/notebook/add_note/')
note_wrap.add_resource(ListNotesResource, '/api/notebook/list_notes/')
note_wrap.add_resource(UpdateNotebookResource, '/api/notebook/update_notebook/')
note_wrap.add_resource(DeleteNotebookResource, '/api/notebook/delete_notebook/')
