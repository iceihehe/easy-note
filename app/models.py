# -*- coding: utf-8 -*-

import datetime

from mongoengine import DynamicDocument, StringField, BooleanField, DateTimeField
from flask_login import UserMixin

from .extensions import bcrypt


class User(DynamicDocument, UserMixin):
    """用户"""

    username = StringField(unique=True)
    password = StringField()

    create_time = DateTimeField(default=datetime.datetime.now)
    last_login = DateTimeField()

    is_delete = BooleanField(default=False)

    meta = {
        'db_alias': 'default',
        'collection': 'users',
        'index_background': True,
    }

    def check_password(self, password):
        """校验密码"""

        if isinstance(password, bytes):
            password = password.decode()

        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def gen_password(password):
        """生成密码"""

        if isinstance(password, str):
            password = password.encode()

        return bcrypt.generate_password_hash(password).decode()
