# encoding: utf-8
from flask_restful import Resource, reqparse, fields, marshal_with
from app.service.BaseService import *
from . import apiv1


class Test(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rate')
        args = parser.parse_args()
        return {'hello': args}, 201, {'fuck': 'you'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=int, location='from')
        args = parser.parse_args()
        return {'hello': args}, 200


class PostsApi(Resource):
    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('category_id', type=int, location='args')
        # self.get_parser.add_argument('tag_id', type=str, location='args')
        self.get_parser.add_argument('limit', type=int, location='args')

        self.post_parser = reqparse.RequestParser()
        # Defaults type to unicode in python2 and str in python3
        self.post_parser.add_argument('title', location='json', required=True)
        self.post_parser.add_argument('body', location='json', required=True)
        self.post_parser.add_argument('slug', location='json')
        self.post_parser.add_argument('tag_ids', type=list, location='json')
        self.post_parser.add_argument('category_id', location='json',
                                      default=1)

    def get(self):
        parser = self.get_parser.parse_args()
        pservice = PostService()
        # lklk
        s = pservice.get_list(**parser)

        return a

    def post(self):
        a = self.post_parser.parse_args()

        return a


def fuck():
    pass
