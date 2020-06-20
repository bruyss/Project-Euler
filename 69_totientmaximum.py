#! python3

from typicals import relprime

def phi(x):
    return sum(map(lambda y: relprime(x, y), range(1, x)))

nmax = 0
divmax= 0
limit = 1000

for n in range(2, limit + 1):
    div = n / phi(n)
    if div > divmax:
        divmax = div
        nmax = n
        print(divmax, nmax)
