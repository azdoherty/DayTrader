from unittest import TestCase

from sqlalchemy import create_engine
import psycopg2

from models import get_connection_string


class TestDb(TestCase):

    def test_connection_string(self):
        engine = create_engine(get_connection_string())
        connection = engine.connect()
        self.assertEqual(1,1)
