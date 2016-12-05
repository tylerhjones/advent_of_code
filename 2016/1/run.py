from shared import *
import numpy as np

input_ary = read_input('input.txt')

inputcords = input_ary[0].replace(" ", "").split(',')



degrees = 90
y = 0
x = 0

grid = np.zeros((1000, 1000), dtype=np.int) # part 2

first_inter = None

for cord in inputcords:
    if cord[0] == 'R':
        degrees += -90
    else:
        degrees += 90

    value = int(cord[1:])
    radians = math.radians(degrees)
    y_change = int(math.sin(radians)) * value
    x_change = int(math.cos(radians)) * value

    # additions for part 2
    if not first_inter:
        for i in range (1, value+1):
            if int(math.sin(radians)) == 1:
                if (grid[x][y+i] == 0):
                    grid[x][y + i] = 1
                else:
                    first_inter = (x,y+i)

            elif int(math.sin(radians)) == -1:
                if (grid[x][y-i] == 0):
                    grid[x][y-i] = 1
                else:
                    first_inter = (x,y-i)

            elif int(math.cos(radians)) == 1:
                if (grid[x+i][y] == 0):
                    grid[x+i][y] = 1
                else:
                    first_inter = (x+i,y)

            elif int(math.cos(radians)) == -1:
                if (grid[x-i][y] == 0):
                    grid[x-i][y] = 1
                else:
                    first_inter = (x-i,y)

    y += y_change
    x += x_change

print "Final:"
print abs(x) + abs(y)
print first_inter