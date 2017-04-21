# -*- coding: utf-8 -*-

from flask_restful import Api
from flask import Blueprint


auth = Blueprint('auth', __name__)
auth_wrap = Api(auth)
