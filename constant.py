import dis

def a():
    a_day_time = 86400
    return a_day_time
dis.dis(a)

print "-" * 30

def b():
    a_day_time = 60 * 60 * 24
    return a_day_time
dis.dis(b)

print "a.func_code.co_consts"
print a.func_code.co_consts

print "b.func_code.co_consts"
print b.func_code.co_consts
