# -*- coding: utf-8 -*-

from flask_restful import Api
from flask import Blueprint

from .restfuls import LoginResource, UserInfoResource


auth = Blueprint('auth', __name__)
auth_wrap = Api(auth)

auth_wrap.add_resource(LoginResource, '/api/login/')
auth_wrap.add_resource(UserInfoResource, '/api/user/get_info/')
