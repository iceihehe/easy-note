# -*- coding: utf-8 -*-

from flask_restful import Api
from flask import Blueprint

from .restfuls import AddNotebookResource, AddNoteResource


note = Blueprint('note', __name__)
note_wrap = Api(note)

note_wrap.add_resource(AddNotebookResource, '/api/notebook/add_notebook/')
note_wrap.add_resource(AddNoteResource, '/api/notebook/add_note/')
