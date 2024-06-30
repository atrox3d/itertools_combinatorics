import itertools as it

# it.repeat(object, [n=infinity]
repeater = it.repeat('X', 4)
values = list(repeater)
print(values)
assert values == list('X' * 4)
