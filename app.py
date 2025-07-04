from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from resources.errors import errors
import logging

from config import MONGODB_SETTINGS
from database.db import initialize_db
from middleware import register_jwt_handlers
from routes import initialize_routes
from resources.auth import jwt_blacklist  # Adicione esta linha

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)
# @TODO: Add an URL restriction into the cors configuration
app.config.from_envvar('ENV_FILE_LOCATION')


api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    return jwt_payload["jti"] in jwt_blacklist

logging.debug("Registrando handlers JWT...")
register_jwt_handlers(app, jwt)
initialize_db(MONGODB_SETTINGS)
initialize_routes(api)

if __name__ == "__main__":
    app.run()
