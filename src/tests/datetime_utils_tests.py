import unittest
from datetime import datetime
from common.utilities.datetime_utils import DatetimeUtils

class TestDateTimeUtils(unittest.TestCase):

    def test_get_iso_date_from_epoch(self):
        self.assertEqual(DatetimeUtils.get_iso_date_from_epoch(1611579461), datetime(2021, 1, 25, 12, 57, 41).isoformat())


if __name__ == '__main__':
    unittest.main()