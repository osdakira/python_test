# encoding: utf-8
# http://docs.python.org/library/functions.html#property

import unittest
try:
    from oktest import test, ok
except ImportError:
    import sys
    print u"Require oktest framework"
    sys.exit(0)


class AClass(object):
    def my_setattr(self, x):
        self.__x = x + 1

    def my_getattr(self):
        return self.__x

    x = property(my_getattr, my_setattr)


class BClass(object):
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x + 1


class Test(unittest.TestCase):
    @test("propertyでgetとsetが呼べる")
    def _(self):
        a = AClass()
        a.x = 1
        ok(a.x) == 2

    @test("@propertyで関数を属性アクセス")
    def _(self):
        b = BClass(1)
        ok(b.x) == 2

if __name__ == "__main__":
    unittest.main()
