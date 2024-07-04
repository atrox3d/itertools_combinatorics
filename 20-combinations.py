import itertools as it

data = list('abcd')

def example_combinations(
        data, r=None, expected=None, 
        printer=lambda x:[print(y) for y in x] + [print()]
    ):
    # it.combinations(iterable, combo_length)
    # order doesnt matter: ('a', 'b') == ('b', 'a')
    print(f'{r=}')
    result = list(it.combinations(data, r or len(data)))
    if result:
        printer(result)
    else:
        print(result)
    if expected is not None:
        assert result == expected
    return result

expected = [
#   ('a', 'b', 'c', 'd')
#     |    |    |    |
    ('a', 'b'),#|    |
#     |    +----+    |
    ('a', 'c'),#     |
#     |    +---------+
    ('a', 'd'),#|    |
#     b<-  +----+    |
    ('b', 'c'),#     |
#     |    +---------+
    ('b', 'd'),#     |
#     c<-  +---------+
    ('c', 'd'),
]
example_combinations(data, r=2, expected=expected)


for r in range(10):
    example_combinations(data, r)
