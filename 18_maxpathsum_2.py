#! python3
# Find the maximum total from top to bottom of the triangle below

import logging
import time

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')


def txtreader(filename):
    text_file = open(filename + '.txt', 'r')
    lines = text_file.readlines()
    for l in range(len(lines)):
        line = lines[l].rstrip()
        lines[l] = [int(i) for i in line.split(" ")]
    return lines

lines = txtreader('18_maxpathsum_2')
start = time.time()
sums = lines[len(lines) - 1]
for i in range(len(lines) - 2, -1, -1):
    for j in range(len(lines[i])):
        sums[j] = max([lines[i][j] + sums[j], lines[i][j] + sums[j + 1]])
duration = time.time() - start

print("Max sum: %d - duration: %0.4fs" % (sums[0], duration))
