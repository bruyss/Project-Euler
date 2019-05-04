#! python3
# How many, not necessarily distinct, values of nCr for 1≤n≤100, are greater
# than one-million?

from typicals import comblen

res = 0

for n in range(1, 101):
    combs = set([(n, r) for r in range(1, n + 1)])
    lens = map(lambda x: comblen(x[0], x[1]), combs)
    res += len([x for x in lens if x > 10**6])
    print(f"{n}: {res}")
