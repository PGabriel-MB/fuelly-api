import pycountry
from flask_bcrypt import check_password_hash, generate_password_hash
from mongoengine import fields as me
from datetime import datetime

from .models import BaseDocument
from .Vehicle import Vehicle


class User(BaseDocument):
    name = me.StringField(required=True, unique=True)
    email = me.EmailField(unique=True)
    password = me.StringField(required=True)
    phone = me.StringField(required=True)
    birth_date = me.DateField(required=True)
    vehicles = me.ListField(me.EmbeddedDocumentField(Vehicle))
    country_code = me.StringField(required=True)

    @property
    def country_name(self):
        try:
            country = pycountry.countries.get(alpha_2=self.country_code)
            return country.name
        except AttributeError:
            return "Unknown country"

    def set_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_of_appropriate_age(self, permitted_age: int) -> bool:
        current_date = datetime.now()
        birth_date = datetime.strptime(self.birth_date, '%Y-%m-%d')
        current_age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    
        if current_age >= permitted_age:
            return True
        else:
            return False
