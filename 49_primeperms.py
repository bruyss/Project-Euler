#! python3
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this
# sequence?

from functools import reduce
import math
from itertools import permutations


def atkin(nmax):
    """
    Returns a list of prime numbers below the number "nmax"
    """
    is_prime = dict([(i, False) for i in range(5, nmax + 1)])
    for x in range(1, int(math.sqrt(nmax)) + 1):
        for y in range(1, int(math.sqrt(nmax)) + 1):
            n = 4 * x ** 2 + y ** 2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 + y ** 2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 - y ** 2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax)) + 1):
        if is_prime[n]:
            ik = 1
            while ik * n ** 2 <= nmax:
                is_prime[ik * n ** 2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]:
            pass
        elif i in [2, 3] or is_prime[i]:
            primes.append(i)
        else:
            pass
    return primes


def list2int(l):
    return int(reduce(lambda x, y: str(x) + str(y), l))


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


def checker(p):
    for i, x in enumerate(p):
        for y in p[i + 1:]:
            diff = y - x
            if y + diff in p:
                print(diff)
                return True
    return False


primes = set([x for x in atkin(10001) if x > 1000])
# primes.difference_update({1487, 4817, 8147})

for prime in primes:
    perms = set(map(list2int, permutations(str(prime))))
    prime_perms = list(perms.intersection(primes))
    if len(prime_perms) > 2:
        prime_perms.sort()
        print(prime_perms)
        if checker(prime_perms):
            break
