# -*- coding: utf-8 -*-

import datetime

from bson import ObjectId
from mongoengine import register_connection
from flask_login import AnonymousUserMixin
from flask.json import JSONEncoder
from flask import Flask

from .config import Config
from .extensions import bcrypt, login_manager
from .auth import auth
from .note import note
from .ueditor import ueditor
from .models import User


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):

        if isinstance(obj, ObjectId):
            return str(obj)

        if isinstance(obj, datetime.datetime):
            return int(obj.strftime('%s'))

        return JSONEncoder.default(self, obj)


def create_app():

    app = Flask(Config.PROJECT)
    app.json_encoder = CustomJSONEncoder

    config_app(app)
    config_database(app)
    config_extensions(app)
    config_blueprint(app)

    return app


def config_app(app):

    app.config.from_object(Config)


def config_database(app):

    register_connection('default', host=Config.MONGODB_URI, connect=False)


def config_extensions(app):

    bcrypt.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            # TODO 日志
            return AnonymousUserMixin()

    @login_manager.unauthorized_handler
    def unauthorized():
        # TODO
        pass


def config_blueprint(app):

    app.register_blueprint(auth)
    app.register_blueprint(note)
    app.register_blueprint(ueditor)
