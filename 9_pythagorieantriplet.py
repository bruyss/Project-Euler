#! python3
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt
import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')


def checktriplet(a, b, c):
    return a*a + b*b == c*c


def checksum(a, b, c, s):
    return a + b + c == s


def wholesqrt(x):
    sq = round(sqrt(x))
    x2 = sq*sq
    return x == x2


def winner(a, b, c, s):
    return checksum(a, b, c, s) and checktriplet(a, b, c)


assert(checktriplet(3, 4, 5))
assert(checksum(1, 2, 3, 6))
assert(wholesqrt(9))

som = 1000
a = 0
found = False

while a < som - 2 and not found:
    a += 1
    b = 0
    c = 1
    while b < som - 2 and not found and c > 0:
        b += 1
        c = som - a - b
        logging.debug('%d + %d + %d = 1000' % (a, b, c))
        found = winner(a, b, c, som)

print('[%d, %d, %d] is a Pythagorean triplet with sum of %d\n' % (a, b, c, som))
print('Their product is %d' % (a*b*c))
