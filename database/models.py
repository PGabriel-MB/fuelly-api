from datetime import datetime

from .db import db

class BaseDocument(db.Document):
    meta = {
        'abstract': True
    }

    created_at = db.DateTimeField(default=datetime.utcnow())
    updated_at = db.DateTimeField(default=datetime.utcnow())
