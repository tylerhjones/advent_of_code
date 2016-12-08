from shared import *
import re
import sys
input_ary = read_input('input.txt')

def transpose(a):
    return map(list, zip(*a))

a = []
for i in range(0,6):
    b = []
    for j in range(0,50):
        b.append(0)
    a.append(b)

def get_x_y(s):
    m = s.split(' ')[1].split('x')
    return int(m[0]), int(m[1])


for line in input_ary:
    line = line.rstrip()

    if 'rect' in line:
        x, y = get_x_y(line)

        for i in range(0, y):
            for j in range(0, x):
                a[i][j] = 1
    elif 'column' in line:
        # rotate row y=2 by 48
        m = line.split('=')[1].split(' by ')
        row_index = int(m[0])
        num = int(m[1])

        a = transpose(a)

        for i in range(0, num):
            a[row_index].insert(0,a[row_index].pop(len(a[row_index])-1))
        a = transpose(a)
    else:
        m = line.split('=')[1].split(' by ')
        row_index = int(m[0])
        num = int(m[1])

        for i in range(0, num):
            a[row_index].insert(0,a[row_index].pop(len(a[row_index])-1))

total = 0
for r in a:

    for e in r:
        if e == 0:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('#')
        total+=e
    sys.stdout.write('\n')

print total