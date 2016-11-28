import itertools

distances = {}
cities = []

def get_input():
    with open('input.txt') as f:
        return f.readlines()

def parse_line(line):
    value = line.split(" = ")[1]
    city1 = line.split(" = ")[0].split(" to ")[0]
    city2 = line.split(" = ")[0].split(" to ")[1]
    global distances
    distances[(city1, city2)] = value
    distances[(city2, city1)] = value
    add_city(city1)
    add_city(city2)

def add_city(city):
    global cities
    if city not in cities:
        cities.append(city)


def get_distance(combo):
    global distances
    t = 0

    for i in range(len(combo)-1):
        try:
            value = distances[combo[i], combo[i+1]]
            t+=int(value)
        except Exception, e:
            print e
            print i

    return t

input_text = get_input()
for line in input_text:
    parse_line(line)

combinations = itertools.permutations(cities, len(cities))

t = 0
for combo in combinations:
    d = get_distance(combo)
    if d > t:
        t = d

print t
