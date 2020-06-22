#! python3

from math import factorial


def digfactorial(x):
    digits = [int(d) for d in str(x)]
    return sum(map(factorial, digits))


def cyclelen(x):
    res = {x}
    digfact = digfactorial(x)
    while digfact not in res:
        res.add(digfact)
        digfact = digfactorial(digfact)
    return len(res)

limit = 1000000
n = 0

for i in range(1, limit + 1):
    if cyclelen(i) == 60:
        print(f"Gottem {i}")
        n += 1

print(n)

