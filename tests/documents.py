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

class EmailFieldDocument(Document):
    email_field = EmailField()

class DatetimeFieldDocument(Document):
    datetime_field = DateTimeField()

class UsersEmbeddedDocument(EmbeddedDocument):
    name = StringField()
    age = IntField()

class UsersEmbeddedFieldDocument(Document):
    user = EmbeddedDocumentField(UsersEmbeddedDocument)

class ReferenceFieldDocument(Document):
    reference = ReferenceField(IntegerFieldDocument)

class BasicListFieldDocument(Document):
    int_list_field = ListField(IntField())

class ReferenceListFieldDocument(Document):
    ref_list_field = ListField(ReferenceField(IntegerFieldDocument))

class EmbeddedDocumentListFieldDocument(Document):
    emb_list_field = ListField(EmbeddedDocumentField(UsersEmbeddedDocument))
