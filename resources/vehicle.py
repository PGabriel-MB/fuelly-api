import json

from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import NotUniqueError, FieldDoesNotExist, DoesNotExist, InvalidDocumentError

from database.User import User
from database.Vehicle import Vehicle

from resources.errors import SchemaValidationError, CarAlreadyExistsError, \
InternalServerError

class VehiclesApi(Resource):
    @jwt_required()
    def get(self):
        try:
            vehicles_list = []

            user_id = get_jwt_identity()
            vehicles = User.objects.get(id=user_id).vehicles

            for vehicle in vehicles:
                vehicle_dict = vehicle.to_mongo().to_dict()
                vehicle_dict.pop('_cls', None)
                vehicle_dict.pop('created_at', None)
                vehicle_dict.pop('updated_at', None)
                vehicles_list.append(vehicle_dict)

            vehicles_data = json.dumps({'vehicles': vehicles_list})
            return Response(vehicles_data, mimetype="application/json", status=200)
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)

            user_vehicles = user.vehicles

            result = next((vehicle for vehicle in user_vehicles if vehicle['license_plate'] == body['license_plate']), None)

            if result:
                raise CarAlreadyExistsError
            
            body['owner'] = user_id

            vehicle = Vehicle(**body).save()
            license_plate = vehicle.license_plate
            return {'message': f'Vehicle {license_plate} added succesfully!'}, 200
        except NotUniqueError:
            raise CarAlreadyExistsError
        except FieldDoesNotExist:
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError


class VehicleApi(Resource): 
    @jwt_required()
    def get(self, id):
        try:
            vehicle = Vehicle.objects.get(id=id).to_json()
            return Response(vehicle, mimetype="application/json", status=200)
        except DoesNotExist:
            raise InvalidDocumentError
        except Exception as e:
            raise InternalServerError
    
    @jwt_required()
    def put(self, id):
        try:
            body = request.get_json()
            Vehicle.objects.get(id=id).update(**body)
            return f'Vechicle id: {id} updated succesfully', 200

        except DoesNotExist:
            raise InvalidDocumentError
        except FieldDoesNotExist:
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError
    
    @jwt_required()
    def delete(self, id):
        try:
            vehicle = Vehicle.objects.get(id=id).delete()

            if vehicle is None:
                raise InvalidDocumentError
            
            return f'Vechile id {id} deleted succesfully', 200
        except DoesNotExist:
            raise InvalidDocumentError
        except Exception as e:
            raise InternalServerError