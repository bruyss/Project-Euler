#! python3
# Work out the first ten digits of the sum of following one-hundred 50-digit numbers.

import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.info('Reading text file')
text_file = open('13_largesum.txt', 'r')
numbers = text_file.read().split('\n')
s = 0
for num in numbers:
    s += int(num)
print(s)
