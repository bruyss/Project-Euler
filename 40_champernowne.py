#! python3
# An irrational decimal fraction is created
# by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part,
# find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

champ = ""
i = 1
while len(champ) < 10**7:
    champ += str(i)
    i += 1

res = 1
for i in [10**x - 1 for x in range(7)]:
    res *= int(champ[i])
print(res)
