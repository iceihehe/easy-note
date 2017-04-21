# -*- coding: utf-8 -*-

from flask_restful import Api
from flask import Blueprint

from .restfuls import AddNotebookResource


note = Blueprint('note', __name__)
note_wrap = Api(note)

note_wrap.add_resource(AddNotebookResource, '/api/notebook/add_notebook/')
