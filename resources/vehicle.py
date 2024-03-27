from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from database.Vehicle import Vehicle
from database.User import User

class VehiclesApi(Resource):
    @jwt_required()
    def get(self):
        vehicles = Vehicle.objects.to_json()
        return Response(vehicles, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        vehicle = Vehicle(**body, added_by=user).save()
        user.update(push__vehicle=vehicle)
        user.save()
        id = vehicle.id
        return { 'id': str(id) }, 200

""" class UserApi(Resource):
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
        return Response(user, mimetype="application/json", status=200) """
