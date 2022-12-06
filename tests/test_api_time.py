import unittest
from datetime import datetime, timezone

from exdelphi.api_time import datetime_to_int, int_to_datetime


class TestApiTime(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_for_valid_int_to_datetime(self):
        self.assertEqual(int_to_datetime(0), datetime(1970, 1, 1, tzinfo=timezone.utc))

    def test_for_valid_datetime_to_int(self):
        self.assertEqual(
            datetime_to_int(datetime(2022, 12, 6, 17, 14, 21, tzinfo=timezone.utc)),
            1670346861,
        )
        self.assertEqual(datetime_to_int(datetime(1970, 1, 1, tzinfo=timezone.utc)), 0)
