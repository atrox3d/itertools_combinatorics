import itertools as it

data = list('abc')

def example_permutations(
        data, r=None, expected=None, 
        printer=lambda x:[print(y) for y in x] + [print()]
    ):
    print(f'{r=}')
    # it.permutations(iterable, [perm_length=len(iterable=None)])
    # order matters: ('a', 'b') != ('b', 'a')
    result = list(it.permutations(data, r=r))
    if result:
        printer(result)
    else:
        print('[]')
    if expected is not None:
        assert result == expected
    return result

expected = [
    ('a', 'b', 'c'),
    # |     \  /
    # |     /  \
    ('a', 'c', 'b'),
    # b <-------+
    ('b', 'a', 'c'),
    # |     \  /
    # |     /  \
    ('b', 'c', 'a'),
    # c <--+
    ('c', 'a', 'b'),
    # |     \  /
    # |     /  \
    ('c', 'b', 'a'),
]
example_permutations(data, expected=expected)

for r in range(1, 10):
    example_permutations(data, r=r)