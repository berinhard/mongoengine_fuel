from decimal import Decimal
from mongoengine import base, Document

from test_case import MongoTestCase
from documents import *
from mongoengine_fuel import MongoFuel


class DocumentFuelCreation(MongoTestCase):

    def should_work_for_int_field(self):
        fuel = MongoFuel(IntegerFieldDocument)
        document = fuel.create()

        self.assertIsInstance(document.int_field, int)

    def should_work_for_boolean_field(self):
        fuel = MongoFuel(BooleanFieldDocument)
        document = fuel.create()

        self.assertIn(document.bool_field, [True, False])

    def should_work_for_boolean_field(self):
        fuel = MongoFuel(StringFieldDocument)
        document = fuel.create()

        self.assertIsInstance(document.str_field, str)
        self.assertTrue(document.str_field)

    def should_work_for_float_field(self):
        fuel = MongoFuel(FloatFieldDocument)
        document = fuel.create()

        self.assertIsInstance(document.float_field, float)

    def should_work_for_decimal_field(self):
        fuel = MongoFuel(DecimalFieldDocument)
        document = fuel.create()

        self.assertIsInstance(document.decimal_field, Decimal)

    def should_work_for_url_field(self):
        fuel = MongoFuel(URLFieldDocument)
        document = fuel.create()

        self.assertIsInstance(document.url_field, str)

    def should_not_override_attrs_setted_by_the_user(self):
        fuel = MongoFuel(IntegerFieldDocument)
        document = fuel.create(int_field=3)

        self.assertEqual(document.int_field, 3)

    def should_raise_value_error_if_field_is_not_supported(self):
        class MyField(base.BaseField):
            pass
        class MyDocument(Document):
            my_field = MyField()

        fuel = MongoFuel(MyDocument)

        self.assertRaises(ValueError, fuel.create)

class EmbeddedDocumentFuelCreation(MongoTestCase):

    def must_return_correct_instance(self):
        fuel = MongoFuel(UsersEmbeddedDocument)

        embedded_document = fuel.create()

        self.assertIsInstance(embedded_document, UsersEmbeddedDocument)
        self.assertIsInstance(embedded_document.name, str)
        self.assertIsInstance(embedded_document.age, int)
