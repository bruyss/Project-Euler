#! python3
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

n = 5000
a = 1
b = 1

for i in range(n):
    c = b
    b += a
    a = c
    print(f'{i+3}: {len(str(b))} {b}')
