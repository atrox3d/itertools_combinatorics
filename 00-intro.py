def builtins():
    x = [0, False, 1, None, 2, 3]
    result = list(filter(None, x))
    assert result == [1, 2, 3]
    return result

def powers_of_two():
    value = 1
    while True:
        yield value
        value *= 2

print(builtins())

[print(p) for _, p in zip(range(10), powers_of_two())]
