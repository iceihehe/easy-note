# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_login import login_user

from .parsers import login_parser
from .managers import AuthManager
from ..constants import Code
from ..functions import make_response


class LoginResource(Resource):

    def post(self):
        """登录"""

        req = login_parser.parse_args(strict=True)

        username = req['username']
        password = req['password']

        user = AuthManager.authenticate(username, password)
        if not user:
            return make_response(code=Code.USERNAME_OR_PASSWORD_ERROR)

        login_user(user)

        return make_response()
