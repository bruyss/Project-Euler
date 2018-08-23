#! python3
# Find the sum of the digits in the number 100!


def myfact(n):
    if n < 1:
        return 1
    else:
        return n * myfact(n - 1)


def getdigits(num):
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num = num // 10
    return digits


n = 100
som = sum(getdigits(myfact(n)))
print(som)