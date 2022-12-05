import datetime
import unittest
from exdelphi.api_time import int_to_datetime


class TestApiTime(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_for_valid_int_to_datetime(self):
        self.assertEqual(
            int_to_datetime(0), datetime.datetime(year=1970, month=1, day=1, hour=1)
        )
