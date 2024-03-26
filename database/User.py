
from flask_bcrypt import generate_password_hash, check_password_hash

from .models import BaseModel
from .db import db
from .Vehicle import Vehicle

class User(BaseModel):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(unique=True)
    password = db.StringField(required=True)
    movies = db.ListField(db.ReferenceField('Vehicle', reverse_delete_rule=db.PULL))

    def set_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Vehicle, 'added_by', db.CASCADE)