import itertools as it


cycler = it.cycle(['A', 'B', 'C'])
values = [next(cycler) for _ in range(3*2)]
print(values)
assert values == ['A', 'B', 'C', 'A', 'B', 'C']
