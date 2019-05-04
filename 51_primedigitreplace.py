# By replacing the 1st digit of the 2-digit number *3, it turns out that six
# of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993. Consequently 56003, being the first member of this family
# ,is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

from typicals import atkin
from typicals import is_prime
from itertools import permutations


def replacedigits(x, digits):
    try:
        replaced = set([])
        for d in range(10):
            xs = str(x)
            for idx in digits:
                xs = xs[:int(idx)] + str(d) + xs[int(idx) + 1:]
            if len(str(int(xs))) == len(str(x)):
                replaced.add(int(xs))
        return replaced
    except IndexError as ie:
        print(f"Number {x} tried with digits {digits}")


limit = 10**6
primes = (x for x in atkin(limit) if len(str(x)) > 1)
found = set([])
glen = 8
maxlen = 0
minprime = limit

for p in primes:
    if p not in found:
        for permlength in range(1, len(str(p))):
            for perm in permutations(range(len(str(p))), permlength):
                replaced = set(
                    filter(lambda x: is_prime(x), replacedigits(p, perm)))
                found.update(replaced)
                if (len(replaced) > maxlen or
                        (p < minprime and len(replaced) == maxlen)):
                    maxlen = len(replaced)
                    minprime = min(replaced)
                    print(f"New max {maxlen} for {minprime} {perm}")
        if maxlen >= glen:
            break

print("Done!")
