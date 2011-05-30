from unittest2 import TestCase
from decimal import Decimal
from datetime import datetime

from documents import *
from mongoengine_fuel.generators import *


class IntegerFieldTests(TestCase):

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


class BooleanFiedTests(TestCase):

    def should_create_boolean_value_for_field(self):
        field = BooleanField()
        value = gen_boolean_value(field)

        self.assertIn(value, [True, False])


class StringFieldTests(TestCase):

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


class FloafFieldTests(TestCase):

    def should_create_float_value_for_field_with_no_boundaries(self):
        field = FloatField()
        value = gen_float_value(field)

        self.assertIsInstance(value, float)

    def should_create_float_value_for_field_with_max_value(self):
        field = FloatField(max_value=0.2)
        value = gen_float_value(field)

        self.assertTrue(value <= 0.2)

    def should_create_float_value_for_field_with_min_value(self):
        field = FloatField(min_value=1.8)
        value = gen_float_value(field)

        self.assertTrue(value >= 1.8)

    def should_create_float_value_for_field_with_max_value_equal_0(self):
        field = FloatField(max_value=0)
        value = gen_float_value(field)

        self.assertTrue(value <= 0)

    def should_create_float_value_for_field_with_min_value_equal_0(self):
        field = FloatField(min_value=0)
        value = gen_float_value(field)

        self.assertTrue(value >= 0)

    def should_create_float_value_for_field_with_min_and_max_value(self):
        field = FloatField(min_value=1.8, max_value=3.0)
        value = gen_float_value(field)

        print value
        self.assertTrue(1.8 <= value <= 3.0)

    def should_create_float_value_for_field_with_negative_min_and_max_value(self):
        field = FloatField(min_value=-4.8, max_value=-3.0)
        value = gen_float_value(field)

        self.assertTrue(-4.8 <= value <= -3.0)

    def should_create_float_value_for_field_with_small_interval_between_min_and_max_value(self):
        field = FloatField(min_value=3.12, max_value=3.13)
        value = gen_float_value(field)

        self.assertTrue(3.12 <= value <= 3.13)


class FloafFieldTests(TestCase):

    def should_create_decimal_value_for_field_with_no_boundaries(self):
        field = DecimalField()
        value = gen_decimal_value(field)

        self.assertIsInstance(value, Decimal)


class URLFieldTests(TestCase):

    def should_create_an_random_url(self):
        field = URLField()
        value = gen_url_value(field)

        self.assertIsInstance(value, str)
        self.assertEqual(None, field.validate(value))


class EmailFieldTests(TestCase):

    def should_create_an_random_email(self):
        field = EmailField()
        value = gen_email_value(field)

        self.assertIsInstance(value, str)
        self.assertEqual(None, field.validate(value))


class DateTimeFieldTests(TestCase):

    def should_create_a_datetime_object(self):
        field = DateTimeField()
        value = gen_datetime_value(field)

        self.assertIsInstance(value, datetime)
