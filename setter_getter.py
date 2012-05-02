# encoding: utf-8
# http://docs.python.org/library/functions.html#property

import unittest
try:
    from oktest import test, ok
except ImportError:
    import sys
    print u"Require oktest framework"
    sys.exit(0)


class PropertyOwner(object):
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


class GetAtter(object):
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.getter
    def x(self):
        return self._x + 1


class PropertyTest(unittest.TestCase):
    @test("@x.setterが使える")
    def _(self):
        p = PropertyOwner()
        p.x = 1
        ok(p.x) == 1

    @test("propertyを定義しないとsetterは使えない")
    def _(self):
        def createNoPropertyObject():
            class NoPropery(object):
                """ @properyがないクラスを作る """
                @x.setter
                def x(self, value):
                    self._x = value                
                @x.getter
                def x(self):
                    return self._x
            return NoPropery()
        ok(createNoPropertyObject).raises(NameError)

    @test("継承では使えない")
    def _(self):
        def createExtends():
            class PropertyExtend(PropertyOwner):
                """ 継承して@getterを付けてみる """
                @x.getter
                def x(self):
                    return self._x
            return PropertyExtend()
        ok(createExtends).raises(NameError)

    @test("@x.getattrが優先される")
    def _(self):
        p = GetAtter()
        p.x = 1
        ok(p.x) == 2
        ok(p._x) == 1

if __name__ == "__main__":
    unittest.main()
