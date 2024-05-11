import unittest

from src.validators import is_valid_amount, is_valid_category


class TestValidators(unittest.TestCase):
    def test_is_valid_category(self):
        self.assertTrue(is_valid_category('доход'))
        self.assertTrue(is_valid_category('расход'))
        self.assertTrue(is_valid_category('ДОХОД'))
        self.assertTrue(is_valid_category('Расход'))

        self.assertFalse(is_valid_category('инвестиции'))
        self.assertFalse(is_valid_category(''))
        self.assertFalse(is_valid_category('123'))

    def test_is_valid_amount(self):
        self.assertTrue(is_valid_amount('100'))
        self.assertTrue(is_valid_amount('100.00'))
        self.assertTrue(is_valid_amount('0.99'))

        self.assertFalse(is_valid_amount('-100'))
        self.assertFalse(is_valid_amount('100.999'))
        self.assertFalse(is_valid_amount('abc'))
        self.assertFalse(is_valid_amount(''))

if __name__ == '__main__':
    unittest.main()
