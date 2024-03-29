from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from config import MONGODB_SETTINGS
from database.db import initialize_db

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

from routes import initialize_routes

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


initialize_db(app)
initialize_routes(api)

app.run()
