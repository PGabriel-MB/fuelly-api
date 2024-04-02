from datetime import datetime
from mongoengine import fields as me

class BaseDocument(me.Document):
    meta = {
        'abstract': True
    }

    created_at = me.DateTimeField(default=datetime.utcnow())
    updated_at = me.DateTimeField(default=datetime.utcnow())
