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

    def should_not_override_attrs_setted_by_the_user(self):
        fuel = MongoFuel(IntegerFieldDocument)
        document = fuel.create(int_field=3)

        self.assertEqual(document.int_field, 3)
