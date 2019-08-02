#! python3

# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
# which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are
# cube.

from typicals import list2int
from itertools import permutations

glen = 5
rlen = 0
x = 1002
cubes = {x**3 for x in range(10**5)}

# assert(isperfectcube(41063625))

while rlen != glen:
    x += 1
    cube = x**3
    print(cube)
    perms = map(list2int, permutations(str(cube)))
    perms = {y for y in perms if y >= cube}
    pc = perms & cubes
    rlen = len(pc)
    print(rlen)

print(f'{x}: {cube}')
