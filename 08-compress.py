import itertools as it

def example_compress():
    # it.compress(iterable, selectors)
    # it.filter(predicate, iterable)
    data = [1, 2, 3, 4, 5]
    selectors = [True, False, True, False, True]
    values = list(it.compress(data, selectors))
    print(values)
    assert values == [1, 3, 5]

example_compress()
