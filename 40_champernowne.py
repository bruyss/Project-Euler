#! python3
# An irrational decimal fraction is created
# by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part,
# find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

from itertools import accumulate

prod_digits = [10**x for x in range(7)]
idxs = list(accumulate([0] + [(9 * 10**(x - 1)) * x for x in range(1, 8)]))
print(idxs)

res = []

for d in prod_digits:
    aantal_cijfers = next(i for i, v in enumerate(idxs) if v > d)
    onder_idx = idxs[aantal_cijfers - 1]
    print(f"{aantal_cijfers} {onder_idx}")
    getal_idx = (d - onder_idx + 1) // aantal_cijfers
    print(getal_idx)
