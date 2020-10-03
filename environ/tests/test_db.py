from unittest import TestCase

from dotenv import load_dotenv
load_dotenv(override=True)    # Load environment variables from .env file. Override any existing environment variables.
# but only while this test is running. 

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

