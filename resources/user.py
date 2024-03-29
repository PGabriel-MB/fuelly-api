from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from database.User import User

class UsersApi(Resource):
    @jwt_required()
    def get(self):
        users = User.objects.to_json()
        return Response(users, mimetype="application/json", status=200)

    # def post(self):
    #     body = request.get_json()
    #     movie = User(**body).save()
    #     id = movie.id
    #     return { 'id': str(id) }, 200

class UserApi(Resource):
    @jwt_required()
    def put(self, id):
        body = request.get_json()
        User.objects.get(id=id).update(**body)
        return  f'id {id} updated successfully', 200

    @jwt_required()
    def delete(self, id):
        user = User.objects.get(id=id).delete()
        return f'id {id} deleted successfully', 200

    @jwt_required()
    def get(self, id):
        user = User.objects.get(id=id).to_json()
        return Response(user, mimetype="application/json", status=200)
