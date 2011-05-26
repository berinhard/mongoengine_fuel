from mongoengine import *

class IntegerFieldDocument(Document):
    int_field = IntField()

class BooleanFieldDocument(Document):
    bool_field = BooleanField()
