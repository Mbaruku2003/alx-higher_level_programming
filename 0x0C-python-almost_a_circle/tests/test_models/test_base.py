"""Define a function."""
import unittest
from models.base import Base


class test_Base(unittest.TestCase):
    """Define constractor test case."""

    def test_init(self):
        """Testing for test_init."""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
