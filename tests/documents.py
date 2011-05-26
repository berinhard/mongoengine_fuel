from mongoengine import *

class IntegerFieldDocument(Document):
    int_field = IntField()

class BooleanFieldDocument(Document):
    bool_field = BooleanField()

class StringFieldDocument(Document):
    str_field = StringField()

class FloatFieldDocument(Document):
    float_field = FloatField()
