from mongoengine import *

from generators import *

#This structure is necessary beacuse mongoengine fields aren't hashable objects
fields_generators_set = set([
    (BooleanField, gen_boolean_value),
    (StringField, gen_str_value),
    (FloatField, gen_float_value),
    (DecimalField, gen_decimal_value),
    (IntField, gen_int_value),
    (URLField, gen_url_value),
])

class MongoFuel():

    def __init__(self, document):
        self.document = document
        self.fields = document._fields
        self._fields_generators = fields_generators_set

    def create(self, **attrs):
        for field_name, field in self.fields.items():
            if isinstance(field, ObjectIdField) or field_name in attrs:
                continue

            generator = self._get_generator(field)
            attrs[field_name] = generator(field)

        instance = self.document(**attrs)
        return instance

    def _get_generator(self, field):
        for field_class, generator in self._fields_generators:
            #isinstance method does not work for fields that has
            # other fields as class parents, like URLField and StringField
            if field.__class__ == field_class:
                return generator

        raise ValueError(u"%s isn't supported by mongoengine_fuel!"
            % field.__class__)
