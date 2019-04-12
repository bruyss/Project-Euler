#! python3
# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
# also prime.
# What is the largest n-digit pandigital prime that exists?

from itertools import permutations
from functools import reduce


def is_prime(n):
    if n <= 1:
        return False
    if n in {2, 3}:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def list2int(l):
    return int(reduce(lambda x, y: str(x) + str(y), l))

res = []

for n in range(3, 10):
    for perm in list(permutations(range(1, n), n - 1)):
        perm_int = list2int(perm)
        print(perm_int)
        if is_prime(perm_int):
            res.append(perm_int)
            
print(res)
print(max(res))    
