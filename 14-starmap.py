import itertools as it


def add(x, y):
    return x + y

def example_map():
    xs = [1, 3, 5]
    ys = [2, 4, 6]
    #     3, 7, 11

    result = list(map(add, xs, ys))
    print(result)
    assert result == [3, 7, 11]

def example_starmap():
    points = [(1, 2), (3, 4), (5, 6)]
    #           3,      7,      11
    result = list(it.starmap(add, points))
    print(result)
    assert result == [3, 7, 11]

example_map()
example_starmap()

# comprehension equivalents
xs = [1, 3, 5]
ys = [2, 4, 6]
print([add(x, y) for x, y in zip(xs, ys)])

points = [(1, 2), (3, 4), (5, 6)]
print([add(*point) for point in points])