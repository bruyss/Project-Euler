#! python3
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

n_max = 1000
res_max = 0
res_n = 0

for n in range(1, n_max + 1):
    res = 0
    for a in range(1, n):
        b = a
        while a + b < n:
            c = n - a - b
            # print(f"({a}, {b}, {c})")
            if a**2 + b**2 == c**2:
                print(f"{n}: ({a}, {b}, {c})")
                res += 1
            b += 1
    if res > res_max:
        res_max = res
        res_n = n
        print(f"New max {res_max} for p = {res_n}")
