import test01_base

def b(arg):
    print "now b", arg

test01_base.b = b
test01_base.a(1)
