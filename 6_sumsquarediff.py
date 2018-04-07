#! python3
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')


def sumsquare(n):
    s = 0
    for i in range(n + 1):
        s += i * i
    return s


def squaresum(n):
    s = 0
    for i in range(n + 1):
        s += i
    return s * s


# Constants
upper = 100

sum_of_squares = sumsquare(upper)
square_of_sum = squaresum(upper)
print('The sum of squares is %d' % sum_of_squares)
print('The square of the sum is %d' % square_of_sum)
print('The difference is %d' % (square_of_sum - sum_of_squares))
