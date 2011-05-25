#coding: utf-8
from unittest2 import TestCase

from mongoengine import connect

class MongoTestCase(TestCase):
    """
    TestCase class that clear the collection between the tests
    """
    def __init__(self, methodName='runtest'):
        self.db = connect('mongoengine_fuel_test')
        super(MongoTestCase, self).__init__(methodName)

    def _post_teardown(self):
        super(MongoTestCase, self)._post_teardown()
        for collection in self.db.collection_names():
            if collection == 'system.indexes':
                continue
            self.db.drop_collection(collection)
