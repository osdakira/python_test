import ast

tree = ast.parse("1 + 1")
for x in ast.walk(tree):
    print x
print ast.dump(tree)

tree = ast.parse("i = 1; i + 1")
for x in ast.walk(tree):
    print x
print ast.dump(tree)


tree = ast.parse("i = 1; i.real")
for x in ast.walk(tree):
    print x
print ast.dump(tree)

tree = ast.parse("eval('1').real")
for x in ast.walk(tree):
    print x
print ast.dump(tree)
