#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Max integer - Unittest """
    def test_max_int(self):
        result = max_integer([6, 7, 5, 4])
        self.assertEqual(result, 7)
        result = max_integer([13, 2, 1, 5])
        self.assertEqual(result, 13)

    def test_isint(self):
        var = 1
        self.assertTrue(max_integer([var, 2]) == 2)
        x = 7
        self.assertTrue(max_integer([1, x]) == x)

    def test_same_entry(self):
        a = 88
        self.assertEqual(max_integer([a, a, a, a]), a)

    def test_float_int(self):
        self.assertEqual(max_integer([7.0, 6, 5]), 7.0)

    def test_one_entry(self):
        self.assertEqual(max_integer([13]), 13)

    def test_negative_int(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
