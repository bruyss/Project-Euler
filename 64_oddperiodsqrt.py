#! python3
# https://projecteuler.net/problem=64

# How many continued fractions for N≤10000 have an odd period?

from math import sqrt, floor


def continuedrootperiod(n):
    a0 = floor(sqrt(n))
    b = a0
    b0 = a0
    c = n - a0**2
    c0 = c

    if c == 0:
        return 0

    a = floor((a0 + b) / c)
    b = a * c - b
    c = floor((n - b**2) / c)
    i = 1

    while (b != b0) or (c != c0):
        a = floor((a0 + b) / c)
        b = a * c - b
        c = floor((n - b**2) / c)
        i += 1
    return i


res = [n for n in range(10001) if continuedrootperiod(n) % 2 == 1]

print(res)
print(len(res))
