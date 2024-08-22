import pycountry
from datetime import datetime
from mongoengine import fields as me

from .models import BaseDocument
from .User import User
from .VehicleFuelingCosts import VehicleFuelingCosts


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

class Vehicle(BaseDocument):
    license_plate = me.StringField(required=False, unique=False, null=True)
    brand = me.StringField(required=True)
    model = me.StringField(required=True)
    year = me.IntField(required=True)
    color = me.StringField(required=True)
    vehicle_type = me.StringField(choices=VEHICLE_TYPE_CHOICES)
    fuel_type = me.StringField(choices=FUEL_TYPE)
    country_code = me.StringField(required=True)
    owner = me.ReferenceField(User, required=True)
    vehicle_fueling_costs = me.ListField(
        me.EmbeddedDocumentField(VehicleFuelingCosts)
    )

    @property
    def country_name(self):
        try:
            country = pycountry.countries.get(alpha_2=self.country_code)
            return country.name
        except AttributeError:
            return "Unknown"

    meta = {
        'allow_inheritance': True
    }