#! python3
# How many different ways can £2 be made using any number of coins?

from numpy import convolve as conv

# coinvalues = (1, 2, 5, 10, 20, 50, 100, 200)
coinvalues = (1, 2, 3)
polynomials = []

k = 1

for k in range(1, max(coinvalues)):
	poly = [0] * (max(coinvalues) + 1)
	ite = set(range(0, max(coinvalues) + 1, k)) & set(coinvalues)
	print(list(range(0, max(coinvalues) + 1, k)))
	print(ite)
	for i in ite:
		poly[i] = 1
		poly.reverse
		polynomials.append(poly)


print(polynomials)

res = conv(polynomials[0], polynomials[1])
print(res)

for pol in polynomials:
	res = conv(res, pol)

print(res)
print(len(res))
print(res[0])
