#! python3
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

# Data
ones = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
tens = {0: 0,
        10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
        20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}
hundreds = {100: 7}


def getdigits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    return digits


def count_letters(num):
    number_letters = 0
    digits = getdigits(num)
    logging.debug(digits)
    if len(digits) > 2:                             # Add hundreds
        number_letters += ones.get(digits[2]) + hundreds.get(100)
        if digits[0] + digits[1] != 0:
            number_letters += 3                     # 'and'
    if len(digits) > 1:                             # Add tens
        if digits[1] == 1:                          # Case for teens
            number_letters += tens.get(10*digits[1] + digits[0])
        else:
            number_letters += tens.get(10 * digits[1])
            if digits[0] != 0:
                number_letters += ones.get(digits[0])
    if len(digits) == 1:
        number_letters += ones.get(digits[0])
    logging.debug('%d has %d letters' % (num, number_letters))
    return number_letters


assert (getdigits(342) == [2, 4, 3])
assert (count_letters(342) == 23)
assert (count_letters(115) == 20)
assert (count_letters(5) == 4)
assert (count_letters(13) == 8)
assert (count_letters(21) == 9)

s = 0
for i in range(1, 1000):
    logging.debug('Adding %d' % i)
    s += count_letters(i)
s += 11     # one thousand
print(s)
