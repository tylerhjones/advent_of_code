

def get_input():
    with open('input.txt') as f:
        return f.readlines()[0]


class Houses(object):
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.houses = [[0 for j in range(self.width)] for i in range(self.width)]

    def visit_house(self, x, y):
        screen_x = self.get_x_screen_coordinates(x)
        screen_y = self.get_y_screen_coordinates(y)

        # if already visited, add to visit count
        if self.houses[screen_x][screen_y]:
            self.houses[screen_x][screen_y] += 1
        else:
            self.houses[screen_x][screen_y] = 1

    def get_x_screen_coordinates(self, x):
        return int(x + self.width/2)

    def get_y_screen_coordinates(self, y):
        return self.height/2 - y

    def get_number_of_houses_visited(self):
        count = 0
        for row in self.houses:
            for house in row:
                if house > 0:
                    count += 1
        return count


class Location(object):
    def __init__(self):
        global houses
        self.xPosition = 0
        self.yPosition = 0

        # init with a visit to the first house
        houses.visit_house(0, 0)

    def process_character(self, character):
        if character == 'v':
            self.move_location(0, -1)
        elif character == '<':
            self.move_location(-1, 0)
        elif character == '^':
            self.move_location(0, 1)
        elif character == '>':
            self.move_location(1, 0)
        else:
            raise Exception("Unknown character [%s]." % character)

    def move_location(self, x, y):
        global houses
        self.xPosition += x
        self.yPosition += y
        houses.visit_house(self.xPosition, self.yPosition)


input = get_input()

houses = Houses()

robo_location = Location()
santa_location = Location()

i = 0
for c in input:
    if i % 2 == 0:
        santa_location.process_character(c)
    else:
        robo_location.process_character(c)
    i += 1

print houses.get_number_of_houses_visited()
