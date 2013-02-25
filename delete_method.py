class A(object):
    def a(self):
        return "a"

a = A()
assert a.a() == "a"

assert hasattr(A, "a")
delattr(A, "a")
assert not hasattr(A, "a")

try:
    assert a.a() == "a"
except AttributeError:
    pass
