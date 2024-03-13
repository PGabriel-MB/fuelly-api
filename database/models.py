import datetime
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(unique=True)
    password = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now())
    updated_at = db.DateTimeField(default=datetime.datetime.now())

    def set_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)