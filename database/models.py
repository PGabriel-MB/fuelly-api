import datetime
from .db import db

class BaseModel(db.Document):
    meta = {
        'abstract': True
    }

    created_at = db.DateTimeField(default=datetime.datetime.now())
    updated_at = db.DateTimeField(default=datetime.datetime.now())
