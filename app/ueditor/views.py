# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import request, jsonify

from .ueditor_config import config


class UeditorView(MethodView):

    def get(self):
        """获取配置文件的"""

        return jsonify(config)
