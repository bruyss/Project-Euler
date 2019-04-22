#! python3
# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors 
# each. What is the first of these numbers?


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors   


count = 0
x = 0

while True:
    if len(set(prime_factors(x))) == 4:
        count += 1
        if count == 4:
            print(f"Gottem {x - 3}")
            break
    else:
        count = 0
    x += 1
