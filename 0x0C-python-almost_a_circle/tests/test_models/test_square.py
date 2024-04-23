"""Define a square."""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class Test_Squareconstractor(unittest.TestCase):
    def constructor(self):
        s1 = Square(size=10, x=1, y=2, id=12)
        
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 12)

        s2 = Square(size=15, x=3)
        self.assertEqual(s2.height, 15)
        self.assertEqual(s2.width, 15)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 0)
