# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import request, jsonify

from .ueditor_config import config


class UeditorView(MethodView):

    def get(self):
        """获取配置文件的"""

        return jsonify(config)

    def post(self):

        action = request.args.get('action')

        if action in ['uploadimage', 'uploadvideo']:
            pass

        res = {
            'state': 'SUCCESS',
            'url': 'https://imgsa.baidu.com/baike/c0%3Dbaike220%2C5%2C5%2C220%2C73/sign=e9f48019cbef7609280691cd4fb4c8a9/8d5494eef01f3a29c8f5514a9925bc315c607c71.jpg',
            'title': 'nimabi',
            'original': 'caonima',
        }

        return jsonify(res)
