#! python3
# How many routes are there from the top left to bottom right corner of a 20x20 lattice?


def factorial(x):
    f = x
    while x > 1:
        x -= 1
        f *= x
    return f


# Init
lattice_size = 20
fact_lat = factorial(lattice_size)

n = factorial(lattice_size * 2) / (fact_lat*fact_lat)
print(n)
