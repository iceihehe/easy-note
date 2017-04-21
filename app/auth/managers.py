# -*- coding: utf-8 -*-

from ..models import User

class AuthManager(object):

    @classmethod
    def authenticate(cls, username, password):

        try:
            user = User.objects.get(username=username)
        except:
            # TODO 日志
            return

        if user.check_password(password):
            return user
        else:
            # TODO 日志
            return
