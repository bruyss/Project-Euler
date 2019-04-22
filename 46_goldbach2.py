#! python3
# It was proposed by Christian Goldbach that every odd composite number can be 
# written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a 
# prime and twice a square?


def is_prime(n):
    if n <= 1:
        return False
    if n in {2, 3}:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    

def odd_comp():
    n = 3
    while True:
        while is_prime(n):
            n += 2
        yield n
        n += 2
        

def smaller_primes(max):
    for n in range(max, 1, -1):
        if is_prime(n):
            yield n
        

def checker(n):
    for p in smaller_primes(n):
        for s in (x**2 for x in range(n - p)):
            if p + 2 * s == n:
                    print(f"{n} = {p} + 2 * {s} gottem")
                    return False
    return True
    

for n in odd_comp():
    if checker(n):
        print(n)
        break
    