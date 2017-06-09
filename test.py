# coding: utf-8
import compare
import unittest

class Tests(unittest.TestCase):
    def test1(self):
        self.assertIs(
                compare.which_is_larger(1,2),
                2)
    def test2(self):
        self.assertIs(
                compare.which_is_larger(6,3),
                6)
    def test3(self):
        self.assertIsInstance(
                compare.which_is_larger(3,3),
                tuple)
    #TODO write 3 tests for compare.compare_strings()
if __name__ == '__main__':
    unittest.main()
