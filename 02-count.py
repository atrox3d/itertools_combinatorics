import itertools as it

# default it.count(start=0, step=1)
counter = it.count(start=10, step=2)
values = [next(counter) for _ in range(5)]
print(values)
assert values == [10, 12, 14, 16, 18]