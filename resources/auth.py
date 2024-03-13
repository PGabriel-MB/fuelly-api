from flask import request
from flask_restful import Resource

from database.models import User

class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.set_password()
        user.save()
        id = user.id
        return { 'id': str(id) }, 200
