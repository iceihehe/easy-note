# -*- coding: utf-8 -*-

from flask import Blueprint

from .views import CommonView


front = Blueprint('front', __name__)
front.add_url_rule('/', view_func=CommonView.as_view('root'))
front.add_url_rule('/index', view_func=CommonView.as_view('index'))
front.add_url_rule('/edite/<id>', view_func=CommonView.as_view('edite'))
front.add_url_rule('/markdown/<id>', view_func=CommonView.as_view('markdown'))
front.add_url_rule('/signin', view_func=CommonView.as_view('signin'))
front.add_url_rule('/favoriteNotes', view_func=CommonView.as_view('favoriteNotes'))
