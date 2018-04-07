#! python3
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')

# Constants
start = 10
known = [2520]
upper = 20
# answer = upper
divisors = range(upper-1, upper//2, -1)
# divisors = (7, 5, 3)

found = False

for bound in range(start + 1, upper + 1):
    i = 1
    new_min = known[-1]
    logging.debug('Zoeken naar minimum voor %d met ondergrens %d' % (bound, new_min))
    while i < bound and new_min % bound != 0:
        i += 1
        new_min = i*known[-1]
        logging.debug('i = %d' % i)
        logging.debug('nieuw minimum = %d' % new_min)
    known.append(new_min)

print('Het kleinste getal dat geheel deelbaar is door alle getallen tussen 1 en %d is %d' % (upper, known[-1]))

#
# while not found:
#     found = False
#     answer += upper
#     logging.debug('Checking %d' % answer)
#     failed = False
#     for i in divisors:
#         if answer % i != 0:
#             logging.debug('%d has failed' % i)
#             failed = True
#             break
#     if not failed:
#         found = True
#
# print(answer)
# for i in range(2, upper + 1):
#     logging.debug('%d / %d = %.1f' % (answer, i, answer / i))
