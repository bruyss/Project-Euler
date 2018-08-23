#! python3
# Evaluate the sum of all the amicable numbers under 10000

import logging
logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')


def sum_divisors(n):
    s = 0
    for d in range(1, n//2 + 1):
        if n % d == 0:
            s += d
    return s


assert sum_divisors(220) == 284
assert sum_divisors(284) == 220


max = 10000
sums = []
amic_sum = 0

for i in range(1, max+1):
    new = sum_divisors(i)
    sums.append(new)
    if new < i:
        if sums[new - 1] == i:
            amic_sum += new + i
print(amic_sum)
