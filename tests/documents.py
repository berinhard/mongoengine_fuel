from mongoengine import *

class IntegerFieldDocument(Document):
    int_field = IntField()

class IntegerFieldDocumentWithMaxValue(Document):
    int_field = IntField(max_value=5)

class IntegerFieldDocumentWithZeroMaxValue(Document):
    int_field = IntField(max_value=0)

class IntegerFieldDocumentWithMinValue(Document):
    int_field = IntField(min_value=5)

class IntegerFieldDocumentWithZeroMinValue(Document):
    int_field = IntField(min_value=0)

class IntegerFieldDocumentWithMaxAndMinValue(Document):
    int_field = IntField(min_value=5, max_value=10)
