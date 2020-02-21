#! python3
# x**2 – D * y**2 = 1
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest
# value of x is obtained

from math import sqrt

squares = {x**2 for x in range(1, 10**6)}
print("squares")
Ds = {x for x in range(1,1001) if x not in squares}

D = 98
x = 0

for D in Ds:
    print(f"D = {D}")
    x = 0
    while(True):
        x += 1
        # print(x)
        ysq = (x**2 - 1) / D
        if ysq in squares:
            y = int(sqrt(ysq))
            print(f"x = {x}\ny = {y}\n\n")
            break
