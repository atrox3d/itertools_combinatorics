import itertools as it


def example_islice():
    # it.islice(iterable, start, stop, step=1)
    # it.islice(iterable, stop)
    data = range(10)
    sliced = it.islice(data, 2, 8, 2)
    result = list(sliced)
    print(result)

example_islice()
