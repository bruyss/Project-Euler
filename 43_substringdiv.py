#! python3
# 43_substringdiv.py

from itertools import permutations
from functools import reduce

primes = (2, 3, 5, 7, 11, 13, 17)
ls = [(x + 1, x + 4, primes[x]) for x in range(len(primes))]
print(ls)

perms = permutations(range(10), 10)
res = set(map(lambda l: int("".join(map(str, l))), perms))

for min, max, div in ls:
    res = set(filter(lambda x: int(str(x)[min:max]) % div == 0, res))

# res = set(res)
print(res)
print(sum(res))
