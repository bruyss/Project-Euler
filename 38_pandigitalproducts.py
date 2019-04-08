#! python3
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and
# (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

from functools import reduce


def prodcat(n, m):
    """
    Returns the concatenation of n * [1, 2,..., m]
    """
    prods = list(map((lambda x: n * x), list(range(1, m + 1))))
    return int(reduce((lambda x, y: str(x) + str(y)), prods))


def is_pandigital(n):
    if len(str(n)) != 9:
        return False
    else:
        digits = set(str(n)) - {'0'}
        # print(digits)
        if len(digits) == 9:
            return True
        else:
            return False


is_panprod = (lambda x, y: is_pandigital(prodcat(x, y)))
assert(is_panprod(192, 3))
# print(is_panprod(192, 4))

n_max = 10**4
n = 1
res = []

while n < n_max:
    m = 2
    while len(str(prodcat(n, m))) < 10:
        if is_panprod(n, m):
            print(f"{n} x {list(range(1, m + 1))} = {prodcat(n, m)}")
            res.append(prodcat(n, m))
        m += 1
    n += 1

print(f"\nAnswer: {max(res)}")
