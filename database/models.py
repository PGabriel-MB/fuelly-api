import datetime
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(unique=True)
    hash_password = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now())
    updated_at = db.DateTimeField(default=datetime.datetime.now())

    def set_password(self):
        self.hash_password = generate_password_hash(self.hash_password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.hash_password, password)