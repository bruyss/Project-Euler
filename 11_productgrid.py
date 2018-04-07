#! python3
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right,
# or diagonally) in the 20×20 grid?

from functools import reduce
import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')


def txtreader(filename):
    text_file = open(filename + '.txt', 'r')
    lines = text_file.read().split('\n')
    grid = []
    for i in range(len(lines)):
        grid.append(lines[i].split(' '))
    text_file.close()
    return grid


def listprod(list):
    return reduce(lambda x, y: x * y, list)


def getdims(grid):
    row = len(grid)
    col = len(grid[0])
    return (row, col)


def vertcheck(grid):
    row, col = getdims(grid)
    max_product = 0
    max_list = []
    max_coords = [0, 0]
    for x in range(row - length + 1):
        for y in range(col):
            current = []
            logging.debug('Start point (%d,%d)' % (x, y))
            for i in range(length):
                current.append(int(grid[x + i][y]))
            product = listprod(current)
            if product > max_product:
                logging.debug('%d > %d new vertical maximum' % (max_product, product))
                max_product = product
                max_list = current
                max_coords = [x, y]
    return max_product, max_list, max_coords


def horcheck(grid):
    row, col = getdims(grid)
    max_product = 0
    max_list = []
    max_coords = [0, 0]
    for x in range(row):
        for y in range(col - length + 1):
            current = []
            logging.debug('Start point (%d,%d)' % (x, y))
            for i in range(length):
                current.append(int(grid[x][y + i]))
            product = listprod(current)
            if product > max_product:
                logging.debug('%d > %d new horizontal maximum' % (max_product, product))
                max_product = product
                max_list = current
                max_coords = [x, y]
    return max_product, max_list, max_coords


def diagRcheck(grid):
    row, col = getdims(grid)
    max_product = 0
    max_list = []
    max_coords = [0, 0]
    for x in range(row - length + 1):
        for y in range(col - length + 1):
            current = []
            logging.debug('Start point (%d,%d)' % (x, y))
            for i in range(length):
                current.append(int(grid[x + i][y + i]))
            product = listprod(current)
            if product > max_product:
                logging.debug('%d > %d new right diagonal maximum' % (max_product, product))
                max_product = product
                max_list = current
                max_coords = [x, y]
    return max_product, max_list, max_coords


def diagLcheck(grid):
    row, col = getdims(grid)
    max_product = 0
    max_list = []
    max_coords = [0, 0]
    for x in range(row - length + 1):
        for y in range(length - 1, col):
            current = []
            logging.debug('Start point (%d,%d)' % (x, y))
            for i in range(length):
                current.append(int(grid[x + i][y - i]))
            product = listprod(current)
            if product > max_product:
                logging.debug('%d > %d new left diagonal maximum' % (max_product, product))
                max_product = product
                max_list = current
                max_coords = [x, y]
    return max_product, max_list, max_coords


# Constants
length = 6

# Read number grid
grid = txtreader('11_productgrid')
vert = vertcheck(grid)
hor = horcheck(grid)
diagR = diagRcheck(grid)
diagL = diagLcheck(grid)

print(vert)
print(hor)
print(diagR)
print(diagL)
