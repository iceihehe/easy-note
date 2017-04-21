# -*- coding: utf-8 -*-

from flask_restful import reqparse


login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True, location='json')
login_parser.add_argument('password', type=str, required=True, location='json')
