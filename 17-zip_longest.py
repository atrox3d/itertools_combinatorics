import itertools as it

def example_zip_longest():
    # zip_longest(*iterables, fillvalue=None)
    data1 = [1, 2, 3]
    data2 = ['a', 'b']
    result = list(it.zip_longest(data1, data2, fillvalue=''))
    print(result)
    assert result == [(1, 'a'), (2, 'b'), (3, '')]

example_zip_longest()