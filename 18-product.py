import itertools as it

data1 = [1, 2]
data2 = ['a', 'b', 'c']
expected = [
    (1, 'a'), (1, 'b'), (1, 'c'),
    (2, 'a'), (2, 'b'), (2, 'c'),
]
''' generate product of two iterables

               1,        2
            /  |  \   /  |  \ 
           a,  b, c  a,  b,  c
  
           1   1  1  2   2   2
           a   b  c  a   b   c
'''

def example_product(data1, data2, expected):
    ''' generate product of iterables with itertools '''
    # it.product(*iterables, repeat=1)
    # repeat=n means:
    # it.product(*iterables, *iterables, ... [n times])
    #         1a, 1b, 1c, 2a, 2b, 2c
    [print(data) for data in (data1, data2)]
    result = list(it.product(data1, data2))
    [print(combo) for combo in result]
    print()
    assert result == expected
    return result

def forloop_product(data1, data2):
    ''' generate product of iterables with for loop '''
    # the same can be done with nested for loop
    # IF we know how many iterables
    product = []
    for x in data1:
        for y in data2:
            product.append((x, y))
    return product

def comprehension_product(data1, data2):
    ''' generate product of iterables with comprehension '''
    # and from for loop to comprehension is fairly easy
    return  [(x, y) for x in data1 for y in data2]

''' test reliability of the three methods '''
product = example_product(data1, data2, expected)
for_product = forloop_product(data1, data2)
comp_product = comprehension_product(data1, data2)
assert product == for_product == comp_product == expected

''' compare repeat=2 with multiple copies of iterables

                   1, 2
                   |
                   a, b, c
                 /   \ 
               1,        2
            /  |  \   /  |  \ 
           a,  b, c  a,  b,  c
  
           1   1  1  1   1   1
           a   a  a  a   a   a
           1   1  1  2   2   2
           a   b  c  a   b   c
'''
def test_product_repeat(data1, data2, repeat=2):
    ''' test repeat argument of product '''
    result = list(it.product(data1, data2, repeat=repeat))
    [print(data) for data in (data1, data2)]
    [print(combo) for combo in result]
    print()
    return result

def test_product_repeat_iterables(data1, data2):
    ''' simulate repeat argument by passing same iterables two times '''
    result = list(it.product(data1, data2, data1, data2))
    [print(data) for data in (data1, data2)]
    [print(combo) for combo in result]
    print()
    return result

tpr = test_product_repeat(data1, data2, 2)
tpri = test_product_repeat_iterables(data1, data2)
assert tpr == tpri
