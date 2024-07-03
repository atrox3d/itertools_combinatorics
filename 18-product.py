import itertools as it

data1 = [1, 2]
data2 = ['a', 'b', 'c']
expected = [
    (1, 'a'), (1, 'b'), (1, 'c'),
    (2, 'a'), (2, 'b'), (2, 'c'),
]

def print_data(*data):
    for d in data:
        print(d)

def example_product(data1, data2, expected):
    # it.product(*iterables, repeat=1)
    # repeat=n means:
    # it.product(*iterables, *iterables, ... [n times])
    #         1a, 1b, 1c, 2a, 2b, 2c
    print_data(data1, data2)
    result = list(it.product(data1, data2))
    [print(combo) for combo in result]
    print()
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

def test_product_repeat(data1, data2, repeat=1):
    result = list(it.product(data1, data2, repeat=repeat))
    print_data(data1, data2, data1, data2)
    [print(combo) for combo in result]
    print()
    # assert result == expected
    return result

def test_product_repeat_iterables(data1, data2):
    result = list(it.product(data1, data2, data1, data2))
    print_data(data1, data2, data1, data2)
    [print(combo) for combo in result]
    print()
    # assert result == expected
    return result

tpr = test_product_repeat(data1, data2, 2)
tpri = test_product_repeat_iterables(data1, data2)
assert tpr == tpri
