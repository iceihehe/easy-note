# -*- coding: utf-8 -*-

from flask_restful import Api
from flask import Blueprint

from .views import UeditorView


ueditor = Blueprint('ueditor', __name__)
ueditor_wrap = Api(ueditor)

ueditor_wrap.add_resource(UeditorView, '/api/ueditor/')
