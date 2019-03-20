#! python3

S = (1, 2, 5, 10, 20, 50, 100, 200)


def count( n, m ):
    if n < 0 or m < 0:
        return 0
    if n == 0:
        return 1

    return count( n, m - 1 ) + count( n - S[m], m )
	

print(count(200, 7))
