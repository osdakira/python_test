import timeit
print(timeit.timeit("sum(1 for line in open('line0.txt'))"))
print(timeit.timeit("len(open('line0.txt').readlines())"))
