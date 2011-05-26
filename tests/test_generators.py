from test_case import MongoTestCase
from documents import *

from mongoengine_fuel.generators import *

class IntegerFieldTests(MongoTestCase):

    def should_create_int_value_for_field_with_no_boundaries(self):
        field = IntField()
        value = gen_int_value(field)

        self.assertIsInstance(value, int)

    def should_create_int_value_for_field_with_max_value(self):
        field = IntField(max_value=5)
        value = gen_int_value(field)

        self.assertTrue(value <= 5)

    def should_create_int_value_for_field_with_min_value(self):
        field = IntField(min_value=5)
        value = gen_int_value(field)

        self.assertTrue(value >= 5)

    def should_create_int_value_for_field_with_min_and_max_value(self):
        field = IntField(min_value=5, max_value=10)
        value = gen_int_value(field)

        self.assertTrue(5 <= value <= 10)

    def must_work_with_max_value_equal_0(self):
        field = IntField(max_value=0)
        value = gen_int_value(field)

        self.assertTrue(value <= 0)

    def must_work_with_min_value_equal_0(self):
        field = IntField(min_value=0)
        value = gen_int_value(field)

        self.assertTrue(value >= 0)


class BooleanFiedTests(MongoTestCase):

    def should_create_boolean_value_for_field(self):
        field = BooleanField()
        value = gen_boolean_value(field)

        self.assertIn(value, [True, False])


class StringFieldTests(MongoTestCase):

    def should_create_str_value_for_field_with_no_boundaries(self):
        field = StringField()
        value = gen_str_value(field)

        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def should_create_str_value_for_field_with_max_length(self):
        field = StringField(max_length=10)
        value = gen_str_value(field)

        self.assertTrue(len(value) <= 10)

    def should_create_str_value_for_field_with_min_length(self):
        field = StringField(min_length=10)
        value = gen_str_value(field)

        self.assertTrue(len(value) >= 10)

    def should_create_str_value_for_field_with_min_and_max_length(self):
        field = StringField(min_length=10, max_length=20)
        value = gen_str_value(field)

        self.assertTrue(10 <= len(value) <= 20)
