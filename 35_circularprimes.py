#! python3
# The number, 197, is called a circular prime because all rotations of 
# the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 
# 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import math


def atkin(nmax):
    """
    Returns a list of prime numbers below the number "nmax"
    """
    is_prime = dict([(i, False) for i in range(5, nmax + 1)])
    for x in range(1, int(math.sqrt(nmax)) + 1):
        for y in range(1, int(math.sqrt(nmax)) + 1):
            n = 4 * x ** 2 + y ** 2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 + y ** 2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 - y ** 2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax)) + 1):
        if is_prime[n]:
            ik = 1
            while ik * n ** 2 <= nmax:
                is_prime[ik * n ** 2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]:
            pass
        elif i in [2, 3] or is_prime[i]:
            primes.append(i)
        else:
            pass
    return primes
	

def getdigits(num):
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num = num // 10
    return digits
	

def digits2int(digits):
	s = ''
	for digit in digits:
		s += str(digit)
	return int(s)


def rotation(x):
	digits = getdigits(x)
	rotations = []
	if len(digits) == 1:
		return [x]
	else:
		new_rotation = 0
		while new_rotation != x:
			digits.insert(0, digits[-1])
			digits = digits[:-1]
			new_rotation = digits2int(digits)
			rotations.append(new_rotation)
		return rotations
	

limit = 10**6
primes = set(atkin(limit))

circprimes = set([])

for prime in primes:
	rotations = set(rotation(prime))
	if rotations < primes:
		print(prime)
		circprimes |= rotations
	
print(sorted(list(circprimes)))
print(len(circprimes))		