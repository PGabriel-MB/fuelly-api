from flask_bcrypt import check_password_hash, generate_password_hash
from mongoengine import fields as me

from .models import BaseDocument
from .Vehicle import Vehicle


class User(BaseDocument):
    name = me.StringField(required=True, unique=True)
    email = me.EmailField(unique=True)
    password = me.StringField(required=True)
    vehicles = me.ListField(me.EmbeddedDocumentField(Vehicle))

    def set_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
