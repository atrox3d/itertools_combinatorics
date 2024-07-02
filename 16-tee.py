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

def test_tee():
    # tee(iterable, n)
    data = [1, 2, 3, 4, 5]
    it1, it2 = it.tee(data, 2)
    values1 = list(it1)
    data[0] = 0
    values2 = list(it2)
    for x in data, values1, values2:
        print(x)
    # assert values1 == values2 == data


example_tee()

# tee must make a copy of data because changing data doesnt
# affect the iterators
test_tee()

