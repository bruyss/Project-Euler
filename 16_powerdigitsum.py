# python3
# What is the sum of the digits of 2**1000?

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


def getdigits(num):
    logging.debug("Seperating into digits")
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num = num // 10
    logging.debug(digits)
    return digits


# Constants
power = 1000
p = 1
i = 0

while i < power:
    p *= 2
    i += 1
logging.debug('2^%d = %d' % (power, p))

digits = getdigits(p)
s = sum(digits)
print(s)
