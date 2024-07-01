import itertools as it


def example_chain():
    # it.chain(*iterables)
    values = list(it.chain([1, 2, 3], [4, 5], [6, 7, 8]))
    print(values)
    assert values == [1, 2, 3, 4, 5, 6, 7, 8]

def example_chain_from_iterable():
    # it.chain.from_iterable(iterable_of_iterables)
    values = list(it.chain.from_iterable([[1, 2, 3], [4, 5], [6, 7, 8]]))
    print(values)
    assert values == [1, 2, 3, 4, 5, 6, 7, 8]

example_chain()
example_chain_from_iterable()
