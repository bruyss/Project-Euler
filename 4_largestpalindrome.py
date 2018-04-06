#! python3
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')


def getdigits(num):
    logging.debug("Seperating %d into digits" % num)
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num = num // 10
    logging.debug(digits)
    return digits


def ispalindrome(num):
    logging.debug("Checking palindrome status of %d" % num)
    digits = getdigits(num)
    palindrome = 1
    for i in range((len(digits) // 2)):
        logging.debug("Checking %d at %d and %d at %d" % (digits[i], i, digits[-i], len(digits)-i))
        if digits[i] != digits[-i-1]:
            palindrome = 0
            break
    return palindrome


# Number of digits
num_digits = 3

palindromes = []

for i in range((10**num_digits)-1, 0, -1):
    for j in range(i, 0, -1):
        product = i*j
        if ispalindrome(product):
            palindromes.append(product)

largest = max(palindromes)
print("The largest palindrome made from the product of %d digit numbers is %d" % (num_digits, largest))
