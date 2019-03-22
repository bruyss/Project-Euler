#! python3
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic
# in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def getdigits(num):
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num = num // 10
    return digits


def ispalindrome(num):
	digits = getdigits(num)
	return digits == list(reversed(digits))


def base2(num):
    return int("{0:b}".format(num))


limit = 10**6
res = []

for i in range(1, limit + 1):
    if ispalindrome(i):
        if ispalindrome(base2(i)):
            res.append(i)
            print(f'{i}: {base2(i)}')

# print(res)
print(f'Done: {sum(res)}')
