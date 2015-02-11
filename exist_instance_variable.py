import unittest

class A(object):
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

class B(object):
    @property
    def a(self):
        if hasattr(self, "_a"):
            return self._a
        return "b"

    @a.setter
    def a(self, a):
        self._a = a

class ATest(unittest.TestCase):
    def test_undefined_instance_variable_is_error(self):
        a = A()
        self.assertRaises(AttributeError, lambda : a.a)

class BTest(unittest.TestCase):
    def test_undefined_instance_variable_is_constant(self):
        b = B()
        self.assertEqual("b", b.a)

    def test_gettable_instance_variable_after_set(self):
        b = B()
        b.a = "a"
        self.assertEqual("a", b.a)

unittest.main()
