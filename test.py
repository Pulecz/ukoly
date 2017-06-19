# coding: utf-8
import compare
import unittest

class Tests(unittest.TestCase):
    def test_number2_larger(self):
        number1 = 1
        number2 = 2
        self.assertIs(
                compare.which_is_larger(number1, number2),
                number2)
    def test_number1_larger(self):
        number1 = 6
        number2 = 3
        self.assertIs(
                compare.which_is_larger(number1, number2),
                number1)
    def test_both_equal(self):
        number1 = 3
        number2 = 3
        self.assertIsInstance(
                compare.which_is_larger(number1, number2),
                tuple)

    #TODO write 3 tests for compare.compare_strings()
if __name__ == '__main__':
    unittest.main()
