# -*- coding: utf-8 -*-

import datetime

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
            now = datetime.datetime.now()
            user.update(set__last_login=now)
            return user
        else:
            # TODO 日志
            return
