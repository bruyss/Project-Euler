#! python3
# How many different ways can £2 be made using any number of coins?

# coinvalues = (1, 2, 5, 10, 20, 50, 100, 200)
coinvalues = [1, 2, 5]
# coinvalues = list(range(1, 21))

# coinvalues_asc = sorted(coinvalues)
# coinvalues_desc = sorted(coinvalues, reverse = True)

partitions = [[max(coinvalues)] + (len(coinvalues) - 1) * [0]]

while partitions[-1][-1] != 1:
	nz_index = next((i for i, x in enumerate(partitions[-1]) if x), None)
	print(partitions[-1])
	print(nz_index)
	if partitions[-1][nz_index] > 1:
		new_partition = partitions[-1]
		new_partition[nz_index] -= 1
		new_partition[nz_index + 1] += 1
	partitions.append(new_partition)
	print(new_partition)
	input()

print(partitions)