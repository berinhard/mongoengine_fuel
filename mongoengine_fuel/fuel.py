from mongoengine import *

from generators import *

class MongoFuel():

    def __init__(self, document):
        self.document = document
        self.fields = document._fields

    def create(self, **attrs):
        for field_name, field in self.fields.items():
            if isinstance(field, ObjectIdField) or field_name in attrs:
                continue

            if isinstance(field, BooleanField):
                attrs[field_name] = gen_boolean_value(field)
            elif isinstance(field, StringField):
                attrs[field_name] = gen_str_value(field)
            elif isinstance(field, FloatField):
                attrs[field_name] = gen_float_value(field)
            else:
                attrs[field_name] = gen_int_value(field)

        instance = self.document.objects.create(**attrs)
        return instance
