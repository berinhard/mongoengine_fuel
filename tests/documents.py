from mongoengine import *

class IntegerFieldDocument(Document):
    int_field = IntField()

class BooleanFieldDocument(Document):
    bool_field = BooleanField()

class StringFieldDocument(Document):
    str_field = StringField()

class FloatFieldDocument(Document):
    float_field = FloatField()

class DecimalFieldDocument(Document):
    decimal_field = DecimalField()

class URLFieldDocument(Document):
    url_field = URLField()

class UsersEmbeddedDocument(EmbeddedDocument):
    name = StringField()
    age = IntField()

class UsersEmbeddedFieldDocument(Document):
    user = EmbeddedDocumentField(UsersEmbeddedDocument)

class ReferenceFieldDocument(Document):
    reference = ReferenceField(IntegerFieldDocument)
