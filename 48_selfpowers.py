#! python 3
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 1000^1000.

self_powers = [x**x for x in range(1, 1001)]

print(str(sum(self_powers))[-10:])
