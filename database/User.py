from flask_bcrypt import check_password_hash, generate_password_hash

from .models import BaseDocument
from .db import db


class User(BaseDocument):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(unique=True)
    password = db.StringField(required=True)
    vehicles = db.ListField(db.EmbeddedDocumentField('Vehicle'))

    def set_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
