#! python3
# How many different ways can £2 be made using any number of coins?

from numpy import convolve as conv

# coinvalues = (1, 2, 5, 10, 20, 50, 100, 200)
# coinvalues = [1, 2, 5]
coinvalues = list(range(1, 21))

# coinvalues_asc = sorted(coinvalues)
# coinvalues_desc = sorted(coinvalues, reverse = True)

polynomials = []

for i in range(1, max(coinvalues) + 1):
    poly = [1] + [0] * (max(coinvalues))
    cur_coins = list(filter(lambda x: not x % i, coinvalues))
    print(f'{i}: {cur_coins}')
    for coin in cur_coins:
        poly[coin] = 1
    print(poly)
    polynomials.append(poly)

res = [1]

for poly in polynomials:
    res = conv(res, poly)

print(res)
