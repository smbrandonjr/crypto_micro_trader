import unittest
from common.utilities.dict_utils import DictUtils

class TestDictUtils(unittest.TestCase):

    def test_get_form_repeater_group_number(self):
        self.assertEqual(DictUtils.get_form_repeater_group_number("portfolios[0][portfolio_name]"), 0)
        self.assertEqual(DictUtils.get_form_repeater_group_number("somedictionaryname[8675309][portfolio_name]"), 8675309)

    def test_get_form_repeater_key(self):
        self.assertEqual(DictUtils.get_form_repeater_key("portfolios[0][portfolio_name]"), "portfolio_name")

if __name__ == '__main__':
    unittest.main()