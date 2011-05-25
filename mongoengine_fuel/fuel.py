from random import randint, choice
from mongoengine import *

def gen_int_value(field):
    if field.max_value == None:
        max_value = 1000
    else:
        max_value = field.max_value

    if field.min_value == None:
        min_value = -1000
    else:
        min_value = field.min_value

    return randint(min_value, max_value)

def get_boolean_value(field):
    return choice([True, False])

class MongoFuel():

    def __init__(self, document):
        self.document = document
        self.fields = document._fields

    def create(self, **attrs):
        for field_name, field in self.fields.items():
            if isinstance(field, ObjectIdField) or field_name in attrs:
                continue

            if isinstance(field, BooleanField):
                attrs[field_name] = get_boolean_value(field)
            else:
                attrs[field_name] = gen_int_value(field)

        instance = self.document.objects.create(**attrs)
        return instance
