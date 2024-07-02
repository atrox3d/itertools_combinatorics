import itertools as it

def example_tee():
    # tee(iterable, n)
    data = [1, 2, 3, 4, 5]
    it1, it2 = it.tee(data, 2)
    values1 = list(it1)
    values2 = list(it2)
    for x in data, values1, values2:
        print(x)
    assert values1 == values2 == data


example_tee()
