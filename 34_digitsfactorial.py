#! python3
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial 
# of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import log10 as log
from math import floor


def flog(x):
	return floor(log(x))
	

def factorial(x):
    f = x
    while x > 1:
        x -= 1
        f *= x
    return f


def getdigits(num):
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num = num // 10
    return digits


def factsum(x):
	"""
	Sum of the factorials of the digits of a number x
	"""
	return sum(list(map(lambda x: factorial(x), getdigits(x))))


res = []

# while x < 10**6:
	# x_factsum = factsum(x)
	# if x == x_factsum:
		# res.append(x)
		# print(x)
	# if x_factsum < x:
		# x += 1
	# else:
		# p = 1
		
	
	
