# -*- coding: utf-8 -*-

import re

# from flask_restful import inputs


# objectid = inputs.regex('^[0-9a-z]{24}$')

def objectid(value):

    message = 'ciao'
    if not value:
        return None

    pattern = re.compile('^[0-9a-z]{24}$')

    if not pattern.match(value):
        raise ValueError(message)

    return value
