# -*- coding: utf-8 -*-

import datetime

from mongoengine import DynamicDocument, StringField, BooleanField, DateTimeField, ObjectIdField, IntField, ListField
from flask_login import UserMixin

from .extensions import bcrypt


class User(DynamicDocument, UserMixin):
    """用户"""

    username = StringField(unique=True)
    password = StringField()

    create_time = DateTimeField(default=datetime.datetime.now)
    last_login = DateTimeField()

    is_deleted = BooleanField(default=False)

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


class Notebook(DynamicDocument):
    """笔记本"""

    title = StringField()
    number_notes = IntField()

    user_id = ObjectIdField()
    parent_notebook_id = ObjectIdField()

    create_time = DateTimeField(default=datetime.datetime.now)
    last_update = DateTimeField()

    is_deleted = BooleanField(default=False)

    meta = {
        'db_alias': 'default',
        'collection': 'notebooks',
        'index_background': True,
    }


class Note(DynamicDocument):
    """笔记"""

    title = StringField()
    tags = ListField()
    desc = StringField()

    user_id = ObjectIdField()
    notebook_id = ObjectIdField()

    create_time = DateTimeField(default=datetime.datetime.now)
    last_update = DateTimeField()

    is_trash = BooleanField(default=False)
    is_deleted = BooleanField(default=False)

    meta = {
        'db_alias': 'default',
        'collection': 'notes',
        'index_background': True,
    }
