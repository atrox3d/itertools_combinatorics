import itertools as it

data = list('abc')

def example_combinations_with_replacement(
        data, r=None, expected=None, 
        printer=lambda x:[print(y) for y in x] + [print()]
    ):
    # it.combinations_with_replacement(iterable, combo_length)
    # order doesnt matter: ('a', 'b') == ('b', 'a')
    # same element is part of the combo: ('a', 'a')
    print(f'{r=}')
    result = list(it.combinations_with_replacement(data, r or len(data)))
    if result:
        printer(result)
    else:
        print(result)
    if expected is not None:
        assert result == expected
    return result

expected = [
#   ('a', 'b', 'c', 'd')
#     |  \
    ('a', 'a'),
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'b'),
    ('b', 'c'),
    ('c', 'c'),
]
example_combinations_with_replacement(data, r=2, expected=expected)


for r in range(10):
    example_combinations_with_replacement(data, r)
