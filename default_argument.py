# encoding: utf-8
import unittest
from oktest import test, ok


def list_append(val, L=[]):
    L.append(val)
    return L


class Test(unittest.TestCase):
    @test("list.appendは破壊的")
    def _(self):
        L = []
        list_append(1, L)
        ok(L) == [1]
        list_append(2, L)
        ok(L) == [1, 2]

    @test("デフォルト引数はモジュール変数と同じ")
    def _1(self):
        L = list_append(1)
        ok(L) == [1]
        L = list_append(11, [10])
        ok(L) == [10, 11]
        L = list_append(2)
        ok(L) == [1, 2]
