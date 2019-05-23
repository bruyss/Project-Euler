#! python3
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For
# example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
# four primes, 792, represents the lowest sum for a set of four primes with
# this property.

# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

from typicals import prime_gen, is_prime, atkin

glen = 4
mset = set()
mlen = 0
gen = prime_gen(3)
sets = [set([p]) for p in atkin(200)]

while(True):
    p = next(gen)
    sets = list(filter(lambda x: len(x) >= mlen - 1, sets))
    for s in sets:
        sn = s
        rappend = map(lambda x: int(str(x) + str(p)), sn)
        lappend = map(lambda x: int(str(p) + str(x)), sn)
        rprime = all([is_prime(x) for x in rappend])
        lprime = all([is_prime(x) for x in lappend])
        if rprime and lprime:
            sn.add(p)
            print(sn)
            sets.append(sn)
        if len(sn) > mlen:
            mlen = len(sn)
            mset = sn
            print(mset)
    if mlen >= glen:
        break

# print(sets)
print(mset)
print(sum(mset))
