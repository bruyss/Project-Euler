#! python3
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

som = 1
current = 1
dim = 1001
inc = 2

for i in range(dim // 2):
	for j in range(4):
		current += inc
		som += current
	inc += 2

print(f'The sum of diagonals is {som}')
