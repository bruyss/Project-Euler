#! python3
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and 
# product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from math import log10 as log
from math import floor


def getdigits(num):
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num = num // 10
    return digits
	

def is_panprod(ma, mp):
	prod = ma * mp
	digits = getdigits(ma) + getdigits(mp) + getdigits(prod)
	if digits.sort == range(1, 10):
		return prod, True
	else:
		return prod, False
		

def flog(x):
	return floor(log(x))
	

pandigital_products = set([])

for multiplicand in range(1, 10**5 + 1):
	for multiplier in range (10**(8 - flog(multiplicand)), 10**(9 - flog(multiplicand))):
		product, is_pan = is_panprod(multiplicand, multiplier)
		print(f'{multiplicand} x {multiplier} = {product}')
		if is_pan: 
			pandigital_products.append(product)

print(pandigital_products)

			
