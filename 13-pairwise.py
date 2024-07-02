import itertools as it


def example_pairwise():
    # it.pairwise(iterable)
    data = [1, 2, 3, 4, 5]
    pairs = list(it.pairwise(data))
    print(pairs)
    assert pairs == [(1, 2), (2, 3), (3, 4), (4, 5)]

example_pairwise()
