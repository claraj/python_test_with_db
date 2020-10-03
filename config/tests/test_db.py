from unittest import TestCase

# do this before importing any other classes in the program to 
# swap our the database path before any part of the program accesses it 

# use this form of imports,
# import config
# config.db_path = 'new_database.db'
# This way modifies the value in the config module.

# Don't use this form,
# from config import db_path
# db_path = 'test_flower.db'
# this imports only the db_path variable and makes it available to this module,
# and changes to the db_path variable don't affect the config module. 

import config
config.db_path = 'test_flower.db'


import program
from models import Flower

class TestDB(TestCase):

    """ Some example tests. These will use the test database. """

    def test_add_flower(self):
        Flower.delete().execute()
        program.add_flower('Tulip')
        flower = Flower.select().where(Flower.name == 'Tulip').get()
        self.assertEqual(flower.name, 'Tulip')

    
    def test_no_duplicate(self):
        Flower.delete().execute()
        program.add_flower('Tulip')
        program.add_flower('Tulip')
        flower_count = Flower.select().where(Flower.name == 'Tulip').count()
        self.assertEqual(1, flower_count)
        flower = Flower.select().where(Flower.name == 'Tulip').get()
        self.assertEqual(flower.name, 'Tulip')

