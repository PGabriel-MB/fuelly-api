class InternalServerError(Exception):
    ...

class SchemaValidationError(Exception):
    ...

class CarAlreadyExistsError(Exception):
    ...

class UpdatingCarError(Exception):
    ...

class DeletingCarError(Exception):
    ...

class CarNotExistsError(Exception):
    ...

class EmailAlreadyExistsError(Exception):
    ...

class UnauthorizedError(Exception):
    ...

class NotAPhoneNumberError(Exception):
    ...

class AgeNotAllowedError(Exception):
    ...

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "CarAlreadyExistsError": {
        "message": "Car with given name already exists",
        "status": 400
    },
    "UpdatingCarError": {
        "message": "Updating Car added by other is forbidden",
        "status": 403
    },
    "DeletingCarError": {
        "message": "Deleting Car added by other is forbidden",
        "status": 403
    },
    "CarNotExistsError": {
        "message": "Car with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "NotAPhoneNumberError": {
        "message": "Invalid phone number",
        "status": 401
    },
    "AgeNotAllowedError": {
        "message": "The age is not allowed",
        "status": 401
    }
}
