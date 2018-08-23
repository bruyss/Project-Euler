#! python3
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def sum_divisors(n):
    s = 0
    for d in range(1, n//2 + 1):
        if n % d == 0:
            s += d
    return s


def is_abundant(n):
    return n < sum_divisors(n)


max = 28123
abundant = []

for i in range(max):
    if is_abundant(i):
        abundant.append(i)

non_abundant = list(range(1, max))
for i in range(len(abundant)):
    print(abundant[i])
    j = i
    while abundant[i] + abundant[j] < max:
        if abundant[i] + abundant[j] in non_abundant:
            non_abundant.remove(abundant[i] + abundant[j])
        j += 1

print(sum(non_abundant))