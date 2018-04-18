#! python3
# Find the maximum total from top to bottom of the triangle below

import logging
import pprint

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')


def txtreader(filename):
    text_file = open(filename + '.txt', 'r')
    lines = text_file.read().split('\n')
    grid = []
    for i in range(len(lines)):
        grid.append(lines[i].split(' '))
    text_file.close()
    return grid


pyr = txtreader('18_maxpathsum')
formatstr = '{0:0%db}' % len(pyr)
max = 0
max_order = ''
for i in range(2**len(pyr)):
    orderstr = formatstr.format(i)[::-1]
    logging.debug(orderstr)
    s = 0
    idx = 0
    for j in range(len(pyr)):
        logging.debug('Adding %s at (%d,%d)' % (pyr[j][idx], j, idx))
        s += int(pyr[j][idx])
        idx += int(orderstr[j])
    if s > max:
        max = s
        max_order = orderstr
        logging.debug('New max %d' % max)
print('Max is %d at %s' % (max, max_order))
# pprint.pprint(pyr)
