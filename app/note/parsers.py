# -*- coding: utf-8 -*-

from flask_restful import reqparse

from ..validators import objectid


add_notebook_parser = reqparse.RequestParser()
add_notebook_parser.add_argument('title', type=str, location='json', required=True)
add_notebook_parser.add_argument('parent_notebook_id', type=objectid, location='json')

update_notebook_parser = reqparse.RequestParser()
update_notebook_parser.add_argument('notebook_id', type=objectid, location='json', required=True)
update_notebook_parser.add_argument('title', type=str, location='json', required=True)

delete_notebook_parser = reqparse.RequestParser()
delete_notebook_parser.add_argument('notebook_id', type=objectid, location='args')

add_note_parser = reqparse.RequestParser()
add_note_parser.add_argument('title', type=str, location='json')
add_note_parser.add_argument('desc', type=str, location='json')
add_note_parser.add_argument('tags', type=str, location='json')
add_note_parser.add_argument('notebook_id', type=objectid, location='json', required=True)

list_notes_parser= reqparse.RequestParser()
list_notes_parser.add_argument('notebook_id', type=objectid, location='args', required=True)

update_note_parser = reqparse.RequestParser()
update_note_parser.add_argument('note_id', type=objectid, location='json', required=True)
update_note_parser.add_argument('title', type=str, location='json')
update_note_parser.add_argument('desc', type=str, location='json')
update_note_parser.add_argument('tags', type=str, location='json')
