import dis

def a():
    return 1 + 1
dis.dis(a)

print "-" * 30

def b(i):
    j = 1
    return i + j
dis.dis(b)

print "-" * 30

def c():
    b(1)
dis.dis(c)
