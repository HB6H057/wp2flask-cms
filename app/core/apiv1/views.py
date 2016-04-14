# encoding: utf-8
from flask_restful import Resource
from . import apiv1


class Test(Resource):
    def get(self):
        return {'hello': 'world'}

# apiv1.add_resource(Test, '/api/v1/test')
