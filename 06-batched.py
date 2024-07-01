import itertools as it

# new in 3.12
def example_batched(n:int):
    # it.batched(iterable, batch_size)
    values = list(it.batched(range(1, 11), n))
    print(values)
    # assert values == [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, )]

for n in range(1, 15):
    print(n)
    example_batched(n)