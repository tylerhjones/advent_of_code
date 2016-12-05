from shared import *
import numpy as np
input_ary = read_input('input.txt')

pad1 = np.matrix([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])

current_cord = (1,1)
part1 = ''

def min_max(n, x):
    if n > x:
        return x
    elif n < 0:
        return 0
    else:
        return n

def get_new_cord(cord, d, x):
    v = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    return min_max(cord[0]+ v[d][0], x), min_max(cord[1]+ v[d][1], x)

for instruction in input_ary:
    i = instruction.rstrip()
    for direction in i:
        current_cord = get_new_cord(current_cord, direction, 2)

    part1 += str(pad1[current_cord[0], current_cord[1]])

print part1


pad2 = np.matrix([
    ['0','0','1','0','0'],
    ['0','2','3','4','0'],
    ['5','6','7','8','9'],
    ['0','A','B','C','0'],
    ['0','0','D','0','0']
]).tolist()

def min_max_cord(new_cord, old_cord):
    sys.stdout.flush()
    if (pad2[new_cord[0]][new_cord[1]]) == '0':
        return old_cord
    else:
        return new_cord

part2 = ''
current_cord = (2,2)

for instruction in input_ary:
    i = instruction.rstrip()
    for direction in i:
        new_cord = get_new_cord(current_cord, direction, 4)
        current_cord = min_max_cord(new_cord, current_cord)

    part2 += str(pad2[current_cord[0]][current_cord[1]])

print part2