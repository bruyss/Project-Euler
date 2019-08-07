#! python3
# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e

# from math import floor, e
import fractions
from typicals import digitalsum

convergent = 100

coefs = [1] * (convergent - 3)
for i in range(2, len(coefs), 3):
    coefs[i] = 2 * ((i + 4) // 3)

coefs = [2, 1, 2] + coefs
print(coefs)
coefs.reverse()

frac = coefs[1] + fractions.Fraction(1, coefs[0])
for coef in coefs[2:]:
    frac = coef + fractions.Fraction(1, frac)

print(frac)
print(digitalsum(frac.numerator))
