from mongoengine import fields as me
from datetime import datetime

from .Vehicle import Vehicle


class VehicleFuelCosts(me.EmbeddedDocument):
    created_at = me.DateTimeField(default=datetime.utcnow())
    updated_at = me.DateTimeField(default=datetime.utcnow())