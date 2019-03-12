#! python3
#  A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1,
# 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

n = int(1e6)
digits = list(range(10))
permutation = ''


def dec2factoradic(x):
    div = 2
    f = '0'
    while x > 0:
        f = str(x % div) + f
        x //= div
        div += 1
    return f


n_fact = dec2factoradic(n - 1).zfill(10)
print(n_fact)
for i in n_fact:
    permutation += str(digits[int(i)])
    digits.remove(digits[int(i)])
print(f'The {n}th permutation of digits is {permutation}')
