#! python3
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and 
# difference are pentagonal and D = |Pk − Pj| is minimised; what is the value 
# of D?

pent = list([x * (3 * x - 1) // 2 for x in range(1, 10**4)])

# print(pent)

for m, Pk in enumerate(pent):
    for Pj in pent[:m - 1]:
        # print(f"{Pk} {Pj}")
        if Pk + Pj in pent:
            print(f"The sum of {Pk} and {Pj} is pentagonal")
        if Pk - Pj in pent:
            print(f"The difference of {Pk} and {Pj} is pentagonal")
        if Pk + Pj in pent and Pk - Pj in pent:
            print(f"Possible answer {Pk - Pj} for {Pk} and {Pj}")
            input()
    