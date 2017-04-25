# -*- coding: utf-8 -*-

from functools import wraps

def access_history(func):

    @wraps
    def wrapper(*args, **kwargs):

        resp = func(*args, **kwargs)

        return resp
    return wrapper
