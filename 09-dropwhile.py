import itertools as it


def example_dropwhile():
    # it.dropwhile(predicate, iterable)
    data = [1, 2, 3, 4, 5, 1, 2, 3]
    # skip -----> 3, ...
    values = list(it.dropwhile(lambda x: x < 3, data))
    print(values)
    assert values == [3, 4, 5, 1, 2, 3]

example_dropwhile()

