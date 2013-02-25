def a():
    return "a"

assert a() == "a"

module_symbol_table = globals()
del module_symbol_table["a"]

try:
    assert a() == "a"
except NameError:
    pass
