from datetime import datetime
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

class Vehicle(db.EmbeddedDocument):
    brand = db.StringField(required=True)
    model = db.StringField(required=True)
    year = db.IntField(required=True)
    color = db.StringField(required=True)
    price = db.DecimalField(required=True)
    vehicle_type = db.StringField(choices=VEHICLE_TYPE_CHOICES)
    fuel_type = db.StringField(choices=FUEL_TYPE)
    created_at = db.DateTimeField(default=datetime.utcnow())
    updated_at = db.DateTimeField(default=datetime.utcnow())

    meta = {
        'allow_inheritance': True
    }