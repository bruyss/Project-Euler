#! python3

# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
# which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are
# cube.

# import timeit
from typicals import samedigits

glen = 5
rlen = 0
res = 0
x = 1002
cubes = {x**3 for x in range(10**5)}

while rlen != glen:
    x += 1
    cube = x**3
    print(cube)
    # cubes = (x**3 for x in range(10**len(str(cube)), 10**(len(str(cube)) + 1)))
    rlen = len({c for c in cubes if samedigits(c, cube)})
    print(rlen)

print(f'{x}: {cube}')
