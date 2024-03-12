from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt

from config import MONGODB_SETTINGS
from database.db import initialize_db

app = Flask(__name__)
app.config.update(MONGODB_SETTINGS)

from routes import initialize_routes

api = Api(app)
bcrypt = Bcrypt(app)


initialize_db(app)
initialize_routes(api)

app.run()
