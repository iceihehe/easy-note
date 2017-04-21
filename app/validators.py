# -*- coding: utf-8 -*-

from flask_restful import inputs


objectid = inputs.regex('^[0-9a-z]{24}$')
