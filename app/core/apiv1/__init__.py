from flask_restful import Api
apiv1 = Api()

from .views import Test

apiv1.add_resource(Test, '/api/v1/test')
