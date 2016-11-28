import re
import math

lights = [[0 for j in range(1000)] for i in range(1000)]


def get_input():
    with open('input.txt') as f:
        return f.readlines()


class LightInstruction(object):
    def __init__(self, action, cord1, cord2):
        self.action = action
        self.cord1 = self.make_cord_int(cord1)
        self.cord2 = self.make_cord_int(cord2)

    def make_cord_int(self, cord):
        c = cord.split(',')
        c[0] = int(c[0])
        c[1] = int(c[1])
        return c

    def order_coords_smallest_first(self):
        c1_distance = get_coord_distance(self.cord1[0], self.cord1[1])
        c2_distance = get_coord_distance(self.cord2[0], self.cord2[1])
        if c1_distance < c2_distance:
            return self.cord1, self.cord2
        else:
            return self.cord2, self.cord1


def parse_line(text):
    matches = re.findall('^(.*)\s(\d{1,3}\,\d{1,3})\sthrough\s(\d{1,3}\,\d{1,3})$', text)[0]
    return LightInstruction(matches[0], matches[1], matches[2])


def set_light(instruction, x, y):
    global lights
    if instruction.action == 'turn on':
        lights[x][y] += 1
    elif instruction.action == 'turn off':
        lights[x][y] = max([0, lights[x][y]-1])

    elif instruction.action == 'toggle':
        # lights[x][y] = 1 - lights[x][y]
        lights[x][y] += 2
    else:
        raise Exception("invalid action [%s]" % instruction.action)


def count_lights():
    global lights
    count = 0
    for row in lights:
        for light in row:
            count += light

    return count


def get_coord_distance(x, y):
    return math.sqrt((x*x)+(y*y))


def handle_instruction(instruction):
    global lights

    # coords are equal, only one point is changed
    if instruction.cord1 == instruction.cord2:
        set_light(instruction, instruction.cord1[0], instruction.cord1[1])

    smaller_coord = instruction.order_coords_smallest_first()[0]
    larger_coord = instruction.order_coords_smallest_first()[1]

    x_range = larger_coord[0] - smaller_coord[0]
    y_range = larger_coord[1] - smaller_coord[1]

    print 'smaller_coord: %s' % smaller_coord
    print 'larger_coord: %s' % larger_coord
    print '%s -> %s' % (x_range, y_range)
    for x in range(smaller_coord[0], larger_coord[0]+1):
        for y in range(smaller_coord[1], larger_coord[1]+1):
            # print '%s,%s' % (x,y)
            set_light(instruction, x, y)


text = get_input()
test_input = [
    'turn on 0,0 through 999,999',
    'toggle 0,0 through 999,0',
    'turn off 499,499 through 500,500'
]

for line in text:
    instruction = parse_line(line)
    handle_instruction(instruction)
    print count_lights()
