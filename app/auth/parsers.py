# -*- coding: utf-8 -*-

from flask_restful import reqparse


login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True, location='json')
login_parser.add_argument('password', type=str, required=True, location='json')

update_info_parser = reqparse.RequestParser()
update_info_parser.add_argument('nickname', type=str, location='json')
update_info_parser.add_argument('remark', type=str, location='json')
update_info_parser.add_argument('avatar', type=str, location='json')
update_info_parser.add_argument('gender', type=int, location='json', choices=(0, 1, 2), default=0)
