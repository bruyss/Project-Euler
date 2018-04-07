#! python3
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


# noinspection PyShadowingNames
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


assert (atkin(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

n = 10001
marge = 5000
limit = round((n + marge) * math.log(n + marge))

# limit = 10000

# sieve = list(range(3, limit + 2, 2))
#
# i = 0
#
# while sieve[i] < math.sqrt(limit):
#     logging.debug('Checking multiples of %d' % sieve[i])
#     for j in sieve[(i+1):]:
#         logging.debug('%d and %d' % (j, sieve[i]))
#         if j % sieve[i] == 0:
#             sieve.remove(j)
#             logging.debug('Removed %d from sieve' % j)
#     i += 1
#     logging.debug("Index %d" % i)
#
# # print('The %d th prime is %d' % (n, sieve[n+1]))
# print('Length list %d' % len(sieve))
# print(sieve[n-1])

primes = atkin(limit)
print("The %d th prime is %d" % (n, primes[n - 1]))