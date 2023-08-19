#!/usr/bin/python3
import unittest
from models.base import Base

class TestBaseId(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_no_args(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)

    def test_with_args(self):
        a = Base(5)
        b = Base(10369)
        self.assertEqual(a.id, 5)
        self.assertEqual(b.id, 10369)

    def test_mixed_args(self):
        a = Base(100)
        b = Base()
        c = Base(4)
        d = Base()
        self.assertEqual(a.id, 100)
        self.assertEqual(b.id, 1)
        self.assertEqual(c.id, 4)
        self.assertEqual(d.id, 2)

    def test_None(self):
        a = Base(None)
        self.assertEqual(a.id, 1)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 5)

    def test_access_private_attr(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects

class TestBaseArgType(unittest.TestCase):

    def test_str(self):
        new = Base("25")
        self.assertEqual(new.id, "25")

    def test_float(self):
        new = Base(3.546)
        self.assertEqual(new.id, 3.546)

    def test_bool(self):
        self.assertEqual(Base(True).id, True)

    def test_set(self):
        self.assertEqual(Base({1, 3, 6}).id, {1, 3, 6})

    def test_tuple(self):
        self.assertEqual(Base((1, 2, 3)).id, (1, 2, 3))

    def test_list(self):
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_dict(self):
        self.assertEqual(Base({"s": 5, "o": 8}).id, {"s": 5, "o": 8})


if __name__ == '__main__':
    unittest.main()

