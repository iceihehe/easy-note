# -*- coding: utf-8 -*-

import hashlib

from flask import jsonify
from qiniu import Auth, put_data

from .constants import Code
from .models import History
from .config import Config


def make_response(data=None, code=Code.SUCCESS, msg=None):

    if data is None:
        data = {}

    if msg is None:
        msg = Code.MSG.get(code, '')

    return jsonify({
        'code': code,
        'data': data,
        'msg': msg,
    })


def add_history(note_id, note_title, notebook_id, user):
    """添加历史"""

    History(
        note_id=note_id,
        note_title=note_title,
        notebook_id=notebook_id,
        user_id=user.id,
    ).save()


def upload_file_to_qiniu(filestream, key=None):

    q = Auth(Config.QINIU_ACCESS_KEY, Config.QINIU_SECRET_KEY)

    if not key:
        key = hashlib.md5(filestream).hexdigest()

    token = q.upload_token(Config.QINIU_BUCKET_NAME, key=key)
    ret, info = put_data(token, key, filestream)
    return 'http://%s/%s' % (Config.QINIU_BUCKET_DOMAIN, ret['key'])
