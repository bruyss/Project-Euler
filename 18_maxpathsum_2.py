#! python3
# Find the maximum total from top to bottom of the triangle below

import logging
import pprint
import copy

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


def txtreader(filename):
    text_file = open(filename + '.txt', 'r')
    lines = text_file.read().split('\n')
    grid = []
    for i in range(len(lines)):
        grid.append(list(map(int, lines[i].split(' '))))
    text_file.close()
    return grid


pyr = txtreader('18_maxpathsum_2')

lastsums = {(0, 0): pyr[0][0]}
for i in range(len(pyr) - 1):
    currentsums = {}
    for item in lastsums.items():
        coord = item[0]
        lastsum = item[1]
        logging.debug('%d at %s' % (lastsum, coord))
        coordL = (coord[0] + 1, coord[1])
        nextsumL = lastsum + pyr[coordL[0]][coordL[1]]
        coordR = (coord[0] + 1, coord[1] + 1)
        nextsumR = lastsum + pyr[coordR[0]][coordR[1]]
        logging.debug('Left: %d     Right: %d' % (nextsumL, nextsumR))
        oldL = currentsums.setdefault(coordL, 0)
        oldR = currentsums.setdefault(coordR, 0)
        currentsums[coordL] = max(nextsumL, oldL)
        logging.debug('Added %d' % currentsums[coordL])
        currentsums[coordR] = max(nextsumR, oldR)
        logging.debug('Added %d' % currentsums[coordR])
    lastsums = copy.deepcopy(currentsums)

print(max(lastsums.values()))
