from test_case import MongoTestCase
from documents import *

from mongoengine_fuel import MongoFuel

class IntegerFieldTests(MongoTestCase):

    def should_create_int_value_for_field_with_no_boundaries(self):
        fuel = MongoFuel(IntegerFieldDocument)
        document = fuel.create()

        self.assertTrue(document.int_field)

    def should_create_int_value_for_field_with_max_value(self):
        fuel = MongoFuel(IntegerFieldDocumentWithMaxValue)
        document = fuel.create()

        self.assertTrue(document.int_field <= 5)

    def should_create_int_value_for_field_with_min_value(self):
        fuel = MongoFuel(IntegerFieldDocumentWithMinValue)
        document = fuel.create()

        self.assertTrue(document.int_field >= 5)

    def should_create_int_value_for_field_with_min_and_max_value(self):
        fuel = MongoFuel(IntegerFieldDocumentWithMaxAndMinValue)
        document = fuel.create()

        self.assertTrue(5 <= document.int_field <= 10)

    def should_not_override_attrs_setted_by_the_user(self):
        fuel = MongoFuel(IntegerFieldDocument)
        document = fuel.create(int_field=3)

        self.assertEqual(document.int_field, 3)

    def must_work_with_max_value_equal_0(self):
        fuel = MongoFuel(IntegerFieldDocumentWithZeroMaxValue)
        document = fuel.create()

        self.assertTrue(document.int_field <= 0)

    def must_work_with_min_value_equal_0(self):
        fuel = MongoFuel(IntegerFieldDocumentWithZeroMinValue)
        document = fuel.create()

        self.assertTrue(document.int_field >= 0)
