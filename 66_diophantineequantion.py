#! python3
# x**2 – D * y**2 = 1
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest
# value of x is obtained

from math import sqrt, floor, ceil

Dlim = 1000
xs = []
xmax = 0
Dmax = 0

squares = {x**2 for x in range(ceil(sqrt(Dlim)))}
Ds = set(range(Dlim + 1)) - squares

for D in Ds:
    x = 1
    y = 1
    while x**2 - D * y**2 != 1:
        x += 1
        y = floor(sqrt((x**2 - 1) / D))
    print(f"{x}^2 - {D} * {y}^2 = 1")
    if x >= xmax:
        xmax = x
        Dmax = D
        print(f"New max {xmax} in {Dmax}\n")
