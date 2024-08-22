from mongoengine import fields as me
from datetime import datetime


class VehicleFuelingCosts(me.EmbeddedDocument):
    price = me.DecimalField(min_value=1.00, precision=2, required=True)
    gas_station_location = me.PointField(required=False)
    gas_station_name = me.StringField(required=False)
    created_at = me.DateTimeField(default=datetime.utcnow())
    updated_at = me.DateTimeField(default=datetime.utcnow())