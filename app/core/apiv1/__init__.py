from flask_restful import Api

apiv1 = Api()

from .views import Test, PostsApi

apiv1.add_resource(Test, '/api/v1/test')
apiv1.add_resource(PostsApi, '/api/v1/posts')
