import datetime
from .db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(unique=True)
    hash_password = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now())

    def set_password(self, password):
        self.hash_password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.hash_password, password)