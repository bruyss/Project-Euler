#! python3
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove 
# digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


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
    

def left_truncatable(n):
    if not is_prime(n) or len(str(n)) <= 1:
        return False
    else:
        while len(str(n)) > 1:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True
        

def right_truncatable(n):
    if not is_prime(n) or len(str(n)) <= 1:
        return False
    else:
        while len(str(n)) > 1:
            n = int(str(n)[:-1])
            # print(n)
            if not is_prime(n):
                return False
        return True
        

is_truncable = (lambda x: left_truncatable(x) and right_truncatable(x))
assert(is_truncable(3797))

res = []
n = 11

while len(res) < 11:
	if is_truncable(n):
		print(n)
		res.append(n)
	n += 1
	
print(f"Answer: {sum(res)}")