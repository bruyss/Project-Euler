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
	for x in range(1, n + 1):
		for y in range(x, n + 1):
			for z in range(y, n + 1):
				if sum([x, y, z]) == n:
					if x**2 + y**2 == z**2:
						print(f"{n}: ({x}, {y}, {z})")
						res += 1
				if x**2 + y**2 < z**2:
					break
	if res > res_max:
		res_max = res
		res_n = n
		print(f"New max {res_max} for p = {res_n}")
