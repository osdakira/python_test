# encoding: utf-8
# http://docs.python.org/library/functions.html#property

import unittest
try:
    from oktest import test, ok
except ImportError:
    import sys
    print u"Require oktest framework"
    sys.exit(0)


def my_setattr(ins, x):
    ins._x = x + 1


def my_getattr(ins):
    return ins._x


class PropertyOwner(object):
    x = property(my_getattr, my_setattr)


class PropertyTest(unittest.TestCase):
    @test("propertyでgetとsetが呼べる")
    def _(self):
        p = PropertyOwner()
        p.x = 1
        ok(p.x) == 1

if __name__ == "__main__":
    unittest.main()
