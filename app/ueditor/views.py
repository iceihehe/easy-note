# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import request, jsonify

from .ueditor_config import config
from ..functions import upload_file_to_qiniu


class UeditorView(MethodView):

    def get(self):
        """获取配置文件的"""

        return jsonify(config)

    def post(self):

        action = request.args.get('action')

        if action in ['uploadimage']:
            upfile = request.files.get('upfile')
            if upfile is None:
                return {
                        'state': '没收到文件',
                    }
            url = upload_file_to_qiniu(upfile.stream.read())

            res = {
                'state': 'SUCCESS',
                'url': url,
                'title': upfile.filename,
                'original': upfile.filename,
            }

            return jsonify(res)

        return {
                'state': '还不支持该ueditor组件',
            }
