# -*- coding: utf-8 -*-

from flask import jsonify

from .constants import Code
from .models import History


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
