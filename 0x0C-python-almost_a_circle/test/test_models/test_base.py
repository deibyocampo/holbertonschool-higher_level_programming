#!/usr/bin/python3
""" test module the class Base """
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """ test case class base """

    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base(86)
        self.assertEqual(b5.id, 86)
        b6 = Base(1.2)
        self.assertEquals(b6.id, 1.2)
        b7 = Base([1, 2, 3])
        self.assertEquals(b7.id, [1, 2, 3])
        self.assertEquals(Base('strd').id, 'strd')
        self.assertEquals(Base(-44).id, -44)

if __name___ == '__main__':
    unittest.main()
