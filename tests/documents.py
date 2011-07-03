from datetime import datetime
from decimal import Decimal
from mongoengine import *

class IntegerFieldDocument(Document):
    int_field = IntField(required=True)

class BooleanFieldDocument(Document):
    bool_field = BooleanField(required=True)

class StringFieldDocument(Document):
    str_field = StringField(required=True)

class FloatFieldDocument(Document):
    float_field = FloatField(required=True)

class DecimalFieldDocument(Document):
    decimal_field = DecimalField(required=True)

class URLFieldDocument(Document):
    url_field = URLField(required=True)

class EmailFieldDocument(Document):
    email_field = EmailField(required=True)

class DatetimeFieldDocument(Document):
    datetime_field = DateTimeField(required=True)

class UsersEmbeddedDocument(EmbeddedDocument):
    name = StringField(required=True)
    age = IntField(required=True)

class UsersEmbeddedFieldDocument(Document):
    user = EmbeddedDocumentField(UsersEmbeddedDocument, required=True)

class ReferenceFieldDocument(Document):
    reference = ReferenceField(IntegerFieldDocument, required=True)

class BasicListFieldDocument(Document):
    int_list_field = ListField(IntField(), required=True)

class ReferenceListFieldDocument(Document):
    ref_list_field = ListField(ReferenceField(IntegerFieldDocument), required=True)

class EmbeddedDocumentListFieldDocument(Document):
    emb_list_field = ListField(EmbeddedDocumentField(UsersEmbeddedDocument), required=True)


class DefaultFieldsDocument(Document):
    int_field = IntField(default=0, required=True)
    bool_field = BooleanField(default=False, required=True)
    str_field = StringField(default='default string', required=True)
    float_field = FloatField(default=0.1, required=True)
    decimal_field = DecimalField(default=Decimal(3), required=True)
    url_field = URLField(default='http://test.com', required=True)
    email_field = EmailField(default='test@server.com', required=True)
    datetime_field = DateTimeField(default=datetime(2011, 1, 1), required=True)
    list_field = ListField(IntField(), default=[3], required=True)


class NotRequiredFieldsDocument(Document):
    int_field = IntField(required=False)
    bool_field = BooleanField(required=False)
    str_field = StringField(required=False)
    float_field = FloatField(required=False)
    decimal_field = DecimalField(required=False)
    url_field = URLField(required=False)
    email_field = EmailField(required=False)
    datetime_field = DateTimeField(required=False)
    list_field = ListField(IntField(), required=False)
