#! python3
# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

multipliers = set([2, 3, 4, 5, 6])

x = 1

while True:
    print(x)
    mults = set(map(lambda y: x * y, multipliers))
    digits = list(map(lambda y: set(str(y)), mults))
    # print(mults)
    # print(digits)
    if set(map(lambda y: y == set(str(x)), digits)) == {True}:
        break
    x += 1
