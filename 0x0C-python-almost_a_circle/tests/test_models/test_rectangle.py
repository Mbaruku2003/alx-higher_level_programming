#/usr/bin/python3
"""Define the method used."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Define  the test constructor."""

    def test_constractor(self):
        """DEfinition of constructor."""
        rect = Rectangle(width =10, height=5, x=1, y=2, id=12)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 12)

    def test__str__(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        leo = f"[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(r1.str, leo)
