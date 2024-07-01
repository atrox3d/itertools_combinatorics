import itertools as it


def example_chain():
    # it.chain(*iterables)
    values = list(it.chain([1, 2, 3], [4, 5], [6, 7, 8]))
    print(values)
    assert values == [1, 2, 3, 4, 5, 6, 7, 8]

example_chain()
