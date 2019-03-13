#! python3
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import matplotlib.pyplot as plt


def getdigits(num):
	"""
	Returns the digits of num in a list
	"""
	digits = []
	while num > 0:
	    digits.insert(0, num % 10)
	    num = num // 10
	return digits


def powersum(num, p):
	"""
	Calculates the sum op the p'th power of the elements of a list
	"""
	som = 0
	for x in getdigits(num):
		som += x**p
	return som


def order(x):
	l = getdigits(x)
	return l[0] * (10**(len(l) - 1))


i = 2
power = 5
answers = set([])
powersums = []

for i in range(5000):
	powersums.append(powersum(i, power))

plt.plot(powersums, "bx")
plt.show()


# try:
# 	while powersum(order(i), power) <= i:
# 		print(i)
# 		som = powersum(i, power)
# 		if som == i:
# 			answers.add(i)
# 		i += 1
# except KeyboardInterrupt as e:
# 	print(sum(answers))

# print(answers)
# print(sum(answers))
