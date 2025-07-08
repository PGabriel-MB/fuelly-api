import datetime
import json

from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError

from database.User import User
from .utils import is_phone_number
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
InternalServerError, NotAPhoneNumberError, AgeNotAllowedError, ValidationError as APIValidationError, ExcessiveFieldsError

# Blacklist simples em memória (para produção, use Redis ou banco)
jwt_blacklist = set()

class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            phone = body.get('phone')

            if not is_phone_number(phone):
                raise NotAPhoneNumberError
            
            body['phone'] = f'+{phone}'

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
            raise ExcessiveFieldsError
        except AgeNotAllowedError:
            raise AgeNotAllowedError
        except NotAPhoneNumberError:
            raise NotAPhoneNumberError
        except ValidationError:
            raise APIValidationError
        except ValueError:
            raise APIValidationError
        except Exception as e:
            raise InternalServerError


class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()

            user = User.objects.get(
                email=body.get('email')
            )
            print("########################### TÁ ENTRANDO AQUI ###########################")
            authorized = user.check_password(body.get('password'))

            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)

            data = { 'id': str(user.id) } | { 'token': access_token }

            return Response(json.dumps(data), mimetype="application/json", status=200)
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except TypeError:
            raise APIValidationError
        except Exception as e:
            print("############################## O ERRO É AQUI #################################")
            print(e)
            raise InternalServerError

class LogoutApi(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]  # JWT ID
        jwt_blacklist.add(jti)
        return {"msg": "Logout realizado com sucesso."}, 200