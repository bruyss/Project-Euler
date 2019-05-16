#! python3
# typicals.py - Typical functions used for solving problems

import math
from functools import reduce
# from itertools import combinations


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
    print("Primes generated")
    return primes


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


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prime_gen(s):
    if s <= 2:
        p = 2
        yield p
        p += 1
    else:
        p = s + 1 - (s % 2)
    while(True):
        while not is_prime(p):
            p += 2
        yield p
        p += 2


def comblen(n, r):
    """
    nCr = n! / (r! * (n - r)!)
    """
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))


def ispalindrome(n):
    sn = str(n)
    if len(sn) < 1:
        return False
    else:
        return sn[:len(sn) // 2] == sn[:(len(sn) // 2) - 1 + len(sn) % 2:-1]


def revadd(x):
    """Returns the sum of x and its reverse"""
    return x + int(str(x)[::-1])


def digitalsum(x):
    """Sum of the digits in x"""
    return int(reduce(lambda x, y: int(x) + int(y), list(str(x))))
