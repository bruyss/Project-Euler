#! python3
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
# first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

# Initialize
upper = 4 * 1e6
a = 0
b = 1
fib = 1
s = 0

while fib < upper:
    if fib % 2 == 0:
        s += fib
        logging.debug("Current sum value: %d" % s)
    fib = a + b
    logging.debug("Current number: %d" % fib)
    a = b
    b = fib

print("The sum of the terms of the Fibonacci sequence less that %d is %d" % (upper, s))