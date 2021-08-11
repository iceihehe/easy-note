# -*- coding: utf-8 -*-

from flask import render_template
from flask.views import MethodView


class CommonView(MethodView):

    def get(self, *args, **kwargs):

        return  render_template('index.html')
