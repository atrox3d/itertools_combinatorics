import itertools as it

def example_takewhile():
    # it.takewhile(predicate, iterable)
    data = [1, 2, 3, 4, 5, 1, 2, 3]
    # take: 1, 2, skip ---------->
    result = list(it.takewhile(lambda x: x < 3, data))
    print(result)
    assert result == [1, 2]

example_takewhile()
