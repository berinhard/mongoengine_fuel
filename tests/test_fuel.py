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

    def should_work_for_email_field(self):
        fuel = MongoFuel(EmailFieldDocument)
        document = fuel.create()

        self.assertIsInstance(document.email_field, str)

    def should_work_for_embedded_document_field(self):
        fuel = MongoFuel(UsersEmbeddedFieldDocument)
        document = fuel.create()

        self.assertIsInstance(document.user, UsersEmbeddedDocument)

    def should_work_for_reference_field(self):
        fuel = MongoFuel(ReferenceFieldDocument)
        document = fuel.create()

        self.assertIsInstance(document.reference, IntegerFieldDocument)

    def must_create_multiple_values_for_list_field_with_basic_fields(self):
        fuel = MongoFuel(BasicListFieldDocument)
        document = fuel.create()

        self.assertTrue(document.int_list_field)
        self.assertIsInstance(document.int_list_field, list)
        for int_value in document.int_list_field:
            self.assertIsInstance(int_value, int)

    def must_create_multiple_values_for_list_field_with_reference_field(self):
        fuel = MongoFuel(ReferenceListFieldDocument)
        document = fuel.create()

        self.assertTrue(document.ref_list_field)
        self.assertIsInstance(document.ref_list_field, list)
        for ref_value in document.ref_list_field:
            self.assertIsInstance(ref_value, IntegerFieldDocument)

    def must_create_multiple_values_for_list_field_with_embedded_document_field(self):
        fuel = MongoFuel(EmbeddedDocumentListFieldDocument)
        document = fuel.create()

        self.assertTrue(document.emb_list_field)
        self.assertIsInstance(document.emb_list_field, list)
        for emb_value in document.emb_list_field:
            self.assertIsInstance(emb_value, UsersEmbeddedDocument)

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

    def should_persist_document_on_creation(self):
        self.assertEqual(IntegerFieldDocument.objects.count(), 0)

        fuel = MongoFuel(IntegerFieldDocument)
        document = fuel.create()

        self.assertEqual(IntegerFieldDocument.objects.count(), 1)

    def should_not_save_document_if_user_does_not_want_to(self):
        self.assertEqual(IntegerFieldDocument.objects.count(), 0)

        fuel = MongoFuel(IntegerFieldDocument)
        document = fuel.create(persists=False)

        self.assertEqual(IntegerFieldDocument.objects.count(), 0)


class EmbeddedDocumentFuelCreation(MongoTestCase):

    def must_return_correct_instance(self):
        fuel = MongoFuel(UsersEmbeddedDocument)

        embedded_document = fuel.create()

        self.assertIsInstance(embedded_document, UsersEmbeddedDocument)
        self.assertIsInstance(embedded_document.name, str)
        self.assertIsInstance(embedded_document.age, int)
