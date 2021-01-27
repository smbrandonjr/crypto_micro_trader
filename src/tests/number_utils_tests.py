import unittest
from common.utilities.number_utils import NumberUtils

class TestNumberUtils(unittest.TestCase):

    def test_cast_as_shortened_float(self):
        beginning_str = "0.00451276536"
        beginning_float = 0.00451276536
        beginning_int = 19
        self.assertEqual(NumberUtils.cast_as_shortened_float(beginning_str, "0.000010000"), 0.00451)
        self.assertEqual(NumberUtils.cast_as_shortened_float(beginning_float, "0.000010000"), 0.00451)
        self.assertEqual(NumberUtils.cast_as_shortened_float(beginning_int, "0.000010000"), 19.0)

if __name__ == '__main__':
    unittest.main()