import itertools as it

def example_filterfalse():
    # filterfalse(predicate, iterable)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # returns values for lambda == False
    values = list(it.filterfalse(lambda x: x%2 == 0, data))
    print(values)
    assert values == [1, 3, 5, 7, 9]

example_filterfalse()
