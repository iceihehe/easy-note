# -*- coding: utf-8 -*-

from flask import Flask

from .config import Config


def create_app():

    app = Flask(Config.PROJECT)

    config_app(app)

    return app


def config_app(app):

    app.config.from_object(config)


def config_database(app):

    pass
