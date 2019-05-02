#! python3
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

from typicals import atkin

limit = 10**6
primes = atkin(limit)
res = []
max_len = 0
max_prime = 2
max_start = 0

for i, prime in enumerate(primes):
    start = 0
    while start < min([i, 6]):
        som = 0
        j = start
        while som < prime:
            som += primes[j]
            j += 1
        if som == prime:
            print(
                f"{prime} is the sum of {j} primes starting at {primes[start]}"
            )
            if j - start > max_len:
                max_len = j - start
                max_prime = prime
                max_start = start
                print(f"New wiener {max_prime} with a length of {max_len}")
                break
        start += 1

print(
    f"\nBig wiener {max_prime}: {primes[max_start: max_start + max_len + 1]}"
)
