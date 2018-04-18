#! python3
# Find the maximum total from top to bottom of the triangle below

import logging
import pprint

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


def txtreader(filename):
    text_file = open(filename + '.txt', 'r')
    lines = text_file.read().split('\n')
    grid = []
    for i in range(len(lines)):
        grid.append(lines[i].split(' '))
    text_file.close()
    return grid


def getdigits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    return digits


pyr = txtreader('18_maxpathsum')
pprint.pprint(pyr)
