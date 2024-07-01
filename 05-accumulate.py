import itertools as it

# it.accumulate(iterable, func=operator.add)
values = list(it.accumulate([1, 2, 3, 4, 5]))
# 1+0, 2+1, 3+3, 4+6, 5+10
print(values)
assert values == [1, 3, 6, 10, 15]