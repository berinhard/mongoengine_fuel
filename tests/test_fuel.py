from test_case import MongoTestCase
from documents import *

from mongoengine_fuel import MongoFuel

class DocumentFuelCreation(MongoTestCase):

    def should_not_override_attrs_setted_by_the_user(self):
        fuel = MongoFuel(IntegerFieldDocument)
        document = fuel.create(int_field=3)

        self.assertEqual(document.int_field, 3)
