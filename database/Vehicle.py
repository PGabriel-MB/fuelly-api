from .models import BaseModel
from .db import db

VEHICLE_TYPE_CHOICES = [
    'common_car',
    'motorcycle',
    'truck',
    'van'
]

FUEL_TYPE = [
    'flex',
    'gasoline',
    'alcool',
    'hybrid_gasoline',
    'hybrid_alcool',
    'hybrid_flex',
]

class Vehicle(BaseModel):
    brand = db.StringField(required=True)
    model = db.StringField(required=True)
    year = db.IntField(required=True)
    color = db.StringField()
    price = db.DecimalField(required=True)
    vehicle_type = db.StringField(choices=VEHICLE_TYPE_CHOICES)
    fuel_type = db.StringField(choices=FUEL_TYPE)
    driver = db.ReferenceField('User')