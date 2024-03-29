# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import request

from ..functions import make_response, upload_file_to_qiniu
from ..constants import Code


class UploadView(MethodView):

    def post(self):

        upfile = request.files.get('upfile')

        if upfile is None:
            return make_response(code=Code.NO_UPFILE)

        if upfile.content_type not in ['image/png', 'image/jpeg']:
            return make_response(code=Code.NOT_SUPPORTED_FORMAT)

        url = upload_file_to_qiniu(upfile.stream.read())
        return make_response({
                'url': url,
            })
