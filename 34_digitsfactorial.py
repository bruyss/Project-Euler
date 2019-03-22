#! python3
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial 
# of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


def factorial(x):
	if x == 0:
		return 1
	else:
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
x = 3

try:
	while x < 2540160:
		x_factsum = factsum(x)
		# print(f'{x}: {x_factsum}')
		# input()
		if x == x_factsum:
			res.append(x)
			print(x)
		if x_factsum <= x:
			x += 1
		else:
			p = 1
			while factsum(x) > x:
				x = ((x // (10**p)) + 1) * 10**p
				# print(f'{x}: {factsum(x)}')
				p += 1
		# x += 1
except KeyboardInterrupt:
	print('Interupted')
finally:
	print(f'Done: {sum(res)}') # 40730
		
	
	
