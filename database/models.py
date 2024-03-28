import datetime
from flask_bcrypt import generate_password_hash, check_password_hash

from .db import db
from .Vehicle import VEHICLE_TYPE_CHOICES, FUEL_TYPE

class Vehicle(db.Document):
    brand = db.StringField(required=True)
    model = db.StringField(required=True)
    year = db.IntField(required=True)
    color = db.StringField()
    price = db.DecimalField(required=True)
    vehicle_type = db.StringField(choices=VEHICLE_TYPE_CHOICES)
    fuel_type = db.StringField(choices=FUEL_TYPE)
    driver = db.ReferenceField('User')

class User(db.Document):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(unique=True)
    password = db.StringField(required=True)
    movies = db.ListField(db.ReferenceField('Vehicle', reverse_delete_rule=db.PULL))

    def set_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Vehicle, 'added_by', db.CASCADE)