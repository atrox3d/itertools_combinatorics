from itertools import starmap
import operator

def dot_product(u, v):
    pairs = zip(u, v, strict=True)          # (u0, v0), (u1, v1), ...
    products = starmap(operator.mul, pairs) # u0*v0, u1*v1, ...
    result = sum(products)  # u0*v0 + u1*v1 + ...
    return result

def dot_product_better(u, v):
    total = 0
    for vn, un in zip(u, v, strict=True):
        total += vn * un
    return total

print(dot_product([1, 2, 3], [4, 5, 6]))
print(dot_product_better([1, 2, 3], [4, 5, 6]))