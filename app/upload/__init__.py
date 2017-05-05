# -*- coding: utf-8 -*-

from flask import Blueprint

from .views import UploadView


upload = Blueprint('upload', __name__)

upload.add_url_rule('/api/upload/', view_func=UploadView.as_view('upload'))
