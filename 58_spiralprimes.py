#! python3
# Starting with 1 and spiralling anticlockwise in the following way, a square
# spiral with side length 7 is formed.
# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
# If one complete new layer is wrapped around the spiral above, a square spiral
# with side length 9 will be formed. If this process is continued, what is the
# side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

from typicals import is_prime

c = 9
width = 3
primefreq = 1
cornerprimes = 3
total = 4

while primefreq > 0.1:
    width += 2
    new = {c + i * (width - 1) for i in range(1, 5)}
    # print(new)
    c = max(new)
    cornerprimes += len(set(filter(lambda x: is_prime(x), new)))
    total += 4
    primefreq = cornerprimes / total
    print(primefreq)
    # inp = input()

print(width)
