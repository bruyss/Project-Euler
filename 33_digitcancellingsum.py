#! python3
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
# which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

import fractions


def getdigits(num):
    digits = set([])
    while num > 0:
        digits.add(num % 10)
        num = num // 10
    return digits
	

def dumb_simplify(num, denum):
	num_digits = getdigits(num)
	denum_digits = getdigits(denum)
	if len(num_digits) == 2 and len(denum_digits) == 2:
		if num_digits & denum_digits == set():
			return [0, 1]
		elif num_digits & denum_digits == {0}:
			return [0, 1]
		else:
			new_num_digits = num_digits - denum_digits
			new_denum_digits = denum_digits - num_digits
			if 0 in new_denum_digits:
				return [0, 1]
			elif len(new_num_digits) == 0:
				return [0, 1]
			else:
				return [new_num_digits.pop(), new_denum_digits.pop()]
	else:
		return [0, 1]
		
		
res = []

for n in range(10, 100):
	for d in range(n + 1, 100):
		frac = fractions.Fraction(n, d)
		dumb_simp = dumb_simplify(n, d)
		dumb_frac = fractions.Fraction(dumb_simp[0], dumb_simp[1])
		if frac == dumb_frac:
			res.append((n, d))
			print(f'{n}/{d}')
