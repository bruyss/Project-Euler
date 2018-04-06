#! python3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math
import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')


def isprime(p):
    logging.debug("Checking %d for prime status" % p)
    prime = 1
    upper = round(math.sqrt(p)) + 1
    for i in range(2, upper):
        if p % i == 0:
            prime = 0
            break
    return prime


# Constants
number = 600851475143

upper = round(math.sqrt(number))
if number % 2 == 1:
    if upper % 2 == 0:
        upper += 1
logging.debug("Upper bound is: %d" % upper)

p = 1

for i in range(upper, 2, -2):
    logging.debug("Current number: %d" % i)
    if number % i == 0 and isprime(i) == 1:
        p = i
        break

print("The largest prime factor of %d is %d" % (number, p))
