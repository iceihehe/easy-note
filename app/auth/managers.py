# -*- coding: utf-8 -*-

import datetime

from ..models import User
from ..constants import Code


class AuthManager(object):

    @classmethod
    def authenticate(cls, username, password):

        try:
            user = User.objects.get(username=username)
        except:
            # TODO 日志
            return

        if user.check_password(password) and not user.is_deleted:
            now = datetime.datetime.now()
            user.update(set__last_login=now)
            return user
        else:
            # TODO 日志
            return


class UserManager(object):

    @classmethod
    def get_info(cls, user_id=None, user=None):
        """获取用户基本信息"""

        def _detail(u):
            res = {
                'nickname': u.nickname,
                'create_time': u.create_time,
                'last_login': u.last_login,
                'gender': u.gender,
                'remark': u.remark,
                'avatar': u.avatar,
            }
            return res

        if user:
            return _detail(user)

        try:
            user = User.objects.get(id=user_id)
        except:
            # TODO 日志
            return Code.NO_SUCH_USER

        return _detail(user)

    @classmethod
    def update_info(cls, nickname, remark, avatar, gender, user_id=None, user=None):
        """修改用户基本信息"""

        if user is None:
            try:
                user = User.objects.get(id=user_id)
            except:
                # TODO 日志
                return Code.NO_SUCH_USER

        user.update(
                set__nickname=nickname,
                set__remark=remark,
                set__avatar=avatar,
                set__gender=gender,
            )

        return Code.SUCCESS
