# -*- coding: utf-8 -*-

from flask import jsonify

from .constants import Code


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
