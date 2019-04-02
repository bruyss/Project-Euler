#! python3
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and 
# product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
	

def is_panprod(ma, mp):
	prod = ma * mp
	digits = set(str(ma) + str(mp) + str(prod)) - {'0'}
	# print(digits)
	if len(digits) == 9:
		return True
	else:
		return False
	

pandigital_products = set([])
assert(is_panprod(39, 186))

for multiplicand in range(1, 10**5 + 1):
	multiplier = multiplicand + 1
	while len(str(multiplicand) + str(multiplier) + str(multiplicand * multiplier)) <= 9:
		# print(f'{multiplicand} x {multiplier}')
		if is_panprod(multiplicand, multiplier):
			print(f"{multiplicand} x {multiplier} = {multiplicand * multiplier}")
			pandigital_products.add(multiplicand * multiplier)
		multiplier += 1

print(sum(pandigital_products)) # 45228

	
