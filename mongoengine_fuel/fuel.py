from random import randint, choice
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
    (EmailField, gen_email_value),
    (DateTimeField, gen_datetime_value),
])


class MongoFuel():
    '''A factory for mongoengine documents. You should user the classmethod create_one to return an instance of your document.'''

    def __init__(self, document):
        self.document = document
        self.fields = document._fields
        self._fields_generators = fields_generators_set

    @classmethod
    def create_one(cls, document, persists=True, **args):
        '''Returns an instance of the document parameter.
        If persists is True, it saves the document on the database'''

        mongo_fuel = cls(document)
        return mongo_fuel._create(persists=persists, **args)

    @classmethod
    def create_many(cls, document, instances=5, persists=True):
        documents = []
        mongo_fuel = MongoFuel(document)

        for i in range(0, instances):
            documents.append(mongo_fuel._create(persists=persists))

        return documents

    def _create(self, persists=True, **attrs):
        '''Returns an instance of MongoFuel's instance document'''

        for field_name, field in self.fields.items():
            if isinstance(field, ObjectIdField) or field_name in attrs or not field.required:
                continue

            if field.default is not None and \
                    not getattr(field.default, '__call__', None):
                value = field.default
            elif field.choices:
                value = choice(field.choices)
            elif isinstance(field, ListField):
                value = []
                list_field = field.field
                for i in range(0, randint(1, 10)):
                    new_value = self._return_value_for_atomic_field(list_field)
                    value.append(new_value)
            else:
                value = self._return_value_for_atomic_field(field)

            attrs[field_name] = value

        instance = self.document(**attrs)
        if persists and issubclass(self.document, Document):
            instance.save()

        return instance

    def _return_value_for_atomic_field(self, field):
        '''Returns a random value for a given atomic field'''
        if isinstance(field, EmbeddedDocumentField) or isinstance(field, ReferenceField):
            new_fuel = MongoFuel(field.document_type)
            value = new_fuel._create()
        else:
            generator = self._get_generator(field)
            value = generator(field)

        return value

    def _get_generator(self, field):
        '''Returns the function reponsible for creating a value for a given field'''

        for field_class, generator in self._fields_generators:
            #isinstance method does not work for fields that has
            # other fields as class parents, like URLField and StringField
            if field.__class__ == field_class:
                return generator

        raise ValueError(u"%s isn't supported by mongoengine_fuel!"
            % field.__class__)
