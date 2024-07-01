import itertools as it

def example_accumulate(check:list, iterable:list=None, function=None):
    iterable = iterable or [1, 2, 3, 4, 5]
    # it.accumulate(iterable, func=operator.add)
    values = list(it.accumulate(iterable, func=function))
    # 1+0, 2+1, 3+3, 4+6, 5+10
    print(values)
    assert values == check
    return values

example_accumulate([1, 3, 6, 10, 15])
example_accumulate([1, 1, 1, 1, 1], function=min)
example_accumulate([1, 2, 3, 4, 5], function=max)