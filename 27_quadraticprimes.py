#! python3
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
#  for consecutive values of n, starting with n=0


def is_prime(n):
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


assert (is_prime(2) is False)
assert (is_prime(8) is False)
assert (is_prime(23) is True)

max = 0
max_pair = []

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(n * n + a * n + b):
            n += 1
        if n > max:
            max = n
            max_pair = [a, b]

print(max, max_pair)
print(max_pair[0] * max_pair[1])
