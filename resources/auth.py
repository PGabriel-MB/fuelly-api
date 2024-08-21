import datetime
import json

from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError

from database.User import User
from .utils import is_phone_number
from config import MONGODB_SETTINGS
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
InternalServerError, NotAPhoneNumberError, AgeNotAllowedError, ValidationError

class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            phone = body.get('phone')

            if not is_phone_number(phone):
                raise NotAPhoneNumberError
            
            body['phone'] = f'+{phone}'

            print('USUARIO!!!!')
            print(body)

            user = User(**body)

            if not user.is_of_appropriate_age(18):
                raise AgeNotAllowedError

            user.set_password()
            user.save()
            id = user.id
            return { 'id': str(id) }, 200
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except FieldDoesNotExist:
            raise SchemaValidationError
        except AgeNotAllowedError:
            raise AgeNotAllowedError
        except NotAPhoneNumberError:
            raise NotAPhoneNumberError
        except ValidationError:
            raise ValidationError
        except Exception as e:
            raise InternalServerError


class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(
                email=body.get('email')
            )
            user.vehicles
            authorized = user.check_password(body.get('password'))

            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            
            user_dict = user.to_mongo().to_dict()

            user_dict.pop('_id', None)
            user_dict.pop('created_at', None)
            user_dict.pop('updated_at', None)
            user_dict.pop('password', None)

            user_dict['birth_date'] = user_dict['birth_date'].strftime('%Y-%m-%d')

            data = { 'id': str(user.id) } | user_dict | { 'token': access_token }            #return { 'token': access_token }, 200

            return Response(json.dumps(data), mimetype="application/json", status=200)
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            print(e)
            raise InternalServerError