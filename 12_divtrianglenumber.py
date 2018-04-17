#! python3
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number
# would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')


# def primefactors(x):
#     pfactors = {}
#     while x % 2 == 0:
#         pfactors[2] = pfactors.get(2, 0) + 1
#         x //= 2
#     factor = 3
#     while x > 1:
#         while x % factor == 0:
#             pfactors[factor] = pfactors.get(factor, 0) + 1
#             x //= factor
#         factor += 2
#     logging.debug('Prime factors are %s' % pfactors)
#     return pfactors


def countdivisors(x):
    xh = x
    divisors = 1
    h = 0
    while x % 2 == 0:       # Find multiples of 2
        h += 1
        x //= 2
    divisors *= h + 1
    factor = 3
    while x > 1:            # Find multiples of all other primes
        h = 0
        while x % factor == 0:
            h += 1
            x //= factor
        divisors *= h + 1
        factor += 2
    logging.debug('%d has %d divisors' % (xh, divisors))
    return divisors


# Init
limit = 500
num = 1
i = 2

while countdivisors(num) < limit:
    num += i
    i += 1
    logging.debug('Triangle number #%d is %d' % (i - 1, num))

print('The first triangle number with %d divisors is %d' % (limit, num))
