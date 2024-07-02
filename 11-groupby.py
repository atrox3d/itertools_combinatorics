import itertools as it

# numbers = range(1, 7)
# chars = list(it.chain.from_iterable([tuple(it.repeat(x, 2)) for x in list('abc')]))
# print(chars)
# data = list(zip(chars, numbers))
# print(data)

def example_groupby(key=None):
    # it.groupby(iterable, key=None)
    data = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('c', 5), ('a', 6)]
    grouped = it.groupby(data, key=key)
    result = [(k, list(group)) for k, group in grouped]
    [print(k, groups) for k, groups in result]
    print()

example_groupby()
example_groupby(lambda x: x[0])
example_groupby(lambda x: x[1])
example_groupby(lambda x: 'a' if x[0] in list('ab') else 'c')
example_groupby(lambda x: (x[1], x[0]))

