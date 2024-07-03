import itertools as it

data1 = [1, 2]
data2 = ['a', 'b', 'c']
expected = [
    (1, 'a'), (1, 'b'), (1, 'c'),
    (2, 'a'), (2, 'b'), (2, 'c'),
]

def example_product(data1, data2, expected):
    # it.product(*iterables, repeat=1)
    # repeat=n means:
    # it.product(*iterables, *iterables, ... [n times])
    #         1a, 1b, 1c, 2a, 2b, 2c
    result = list(it.product(data1, data2))
    [print(combo) for combo in result]
    assert result == expected
    return result

def forloop_product(data1, data2):
    # the same can be done with nested for loop
    # IF we know how many iterables
    product = []
    for x in data1:
        for y in data2:
            product.append((x, y))
    return product

def comprehension_product(data1, data2):
    # and from for loop to comprehension is fairly easy
    return  [(x, y) for x in data1 for y in data2]

product = example_product(data1, data2, expected)
for_product = forloop_product(data1, data2)
comp_product = comprehension_product(data1, data2)

assert product == for_product == comp_product == expected
