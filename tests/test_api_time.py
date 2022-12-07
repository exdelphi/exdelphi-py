import unittest
from datetime import datetime, timezone

from exdelphi.api_time import datetime_string_to_int, datetime_to_int, int_to_datetime


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

    def test_datetime_string_to_int(self):
        format_string = "%Y-%m-%d %H:%M:%S"
        self.assertEqual(
            datetime_string_to_int("2022-12-06 17:14:21", format_string), 1670346861
        )
        self.assertEqual(
            datetime_string_to_int("1970-01-01 00:00:00", format_string), 0
        )
