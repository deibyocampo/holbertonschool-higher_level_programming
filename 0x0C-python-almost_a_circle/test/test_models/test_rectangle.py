#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """ test case class Rectangle """

    def test_init_rectangle(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle('a', 2)
        with self.assertRaises(TypeError):
            Rectangle([1, 2], 2)
        with self.assertRaises(TypeError):
            Rectangle((1, 2), 2)
        with self.assertRaises(TypeError):
            Rectangle({'1': 'one'}, 2)
        with self.assertRaises(TypeError):
            Rectangle(1.2, 2)
        with self.assertRaises(TypeError):
            Rectangle(-1, 2)
        with self.assertRaises(TypeError):
            Rectangle(0, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1.2)

if __name__ == '__main__':
    unittest.main()
