# -*- coding: utf-8 -*-

from mongoengine import register_connection
from flask import Flask

from .config import Config
from .extensions import bcrypt


def create_app():

    app = Flask(Config.PROJECT)

    config_app(app)
    config_database(app)
    config_extensions(app)

    return app


def config_app(app):

    app.config.from_object(Config)


def config_database(app):

    register_connection('default', host=Config.MONGODB_URI, connect=False)


def config_extensions(app):

    bcrypt.init_app(app)
