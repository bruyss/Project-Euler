#! python3
# It is possible to show that the square root of two can be expressed as an
# infinite continued fraction.

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
# expansion, 1393/985, is the first example where the number of digits in the
# numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator
# with more digits than denominator?

import fractions


def recurroot2(x, n):
    if n == 0:
        return 0
    if n == 1:
        return 3 / 2
    if n == 2:
        return 1 + x
    else:
        return recurroot2(1 / (2 + x), n - 1)


x_prev = fractions.Fraction(1, 2)
res = 0

for i in range(1000):
    x = 1 / (2 + x_prev)
    f = 1 + x
    if len(str(f.numerator)) > len(str(f.denominator)):
        res += 1
    x_prev = x

print(res)
