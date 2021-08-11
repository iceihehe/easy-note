# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_login import login_user, login_required, current_user

from .parsers import login_parser, update_info_parser
from .managers import AuthManager, UserManager
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


class UserInfoResource(Resource):

    @login_required
    def get(self):

        result = UserManager.get_info(user=current_user)

        return make_response(result)

    @login_required
    def post(self):

        req = update_info_parser.parse_args()
        nickname = req['nickname']
        remark = req['remark']
        avatar = req['avatar']
        gender = req['gender']

        result = UserManager.update_info(nickname, remark, avatar, gender, user=current_user)

        return make_response(code=result)
