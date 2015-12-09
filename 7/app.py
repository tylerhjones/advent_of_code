import re
import sys

value_cache = {}

test_input = [
    '123 -> x',
    '456 -> y',
    'x AND y -> d',
    'x OR y -> e',
    'x LSHIFT 2 -> f',
    'y RSHIFT 2 -> g',
    'NOT x -> h',
    'NOT y -> i'
]


def get_input():
    with open('input.txt') as f:
        return f.readlines()


def get_assigned_wire(line):
    return re.findall('.*\s->\s(.+)', line)[0]


def process_line(line):
    if not line:
        print 'recieved none value for line.'
        sys.exit(1)

    global value_cache
    if get_assigned_wire(line) in value_cache:
        return value_cache[get_assigned_wire(line)]

    elif is_gate_action(line):
        return process_gate(line)

    elif is_wire_assignment(line):
        return process_wire_assignment(line)

    elif is_not_action(line):
        return process_not_gate(line)

    elif is_wire_input(line):
        return process_wire_input(line)

    else:
        print 'Unable to process line [%s]' % line
        sys.exit(1)


def process_wire_input(line):
    global value_cache
    wire_value = re.findall('([0-9]+)\s->\s', line)[0]
    value_cache[get_assigned_wire(line)] = int(wire_value)
    return int(wire_value)


def process_wire_assignment(line):
    wire = re.findall('([a-z]+)\s->\s', line)[0]
    return process_line(lines[wire])


def process_not_gate(line):
    wire = re.findall('NOT\s([a-z]+)\s->\s', line)[0]
    value = process_line(lines[wire])
    return (~value) & 0b1111111111111111


def process_gate(line):
    input1, action, input2 = re.findall('([a-z0-9]+)\s([A-Z]+)\s([a-z0-9]+)\s->\s', line)[0]
    return get_gate_output(action, input1, input2, line)


def get_value(key):
    global value_cache
    if key.isdigit():
        return int(key)
    else:
        return process_line(lines[key])


def get_gate_output(action, input1, input2, line):
    global value_cache
    if get_assigned_wire(line) in value_cache:
        return value_cache[get_assigned_wire(line)]

    if action == 'RSHIFT':
        value = get_value(input1) >> get_value(input2)
    elif action == 'AND':
        value = get_value(input1) & get_value(input2)
    elif action == 'LSHIFT':
        value = get_value(input1) << get_value(input2)
    elif action == 'OR':
        value = get_value(input1) | get_value(input2)
    else:
        raise Exception("Undefined gate self.action [%s]" % action)
    value_cache[get_assigned_wire(line)] = value
    return value


def is_gate_action(line):
    return re.match('^[0-9a-z]+\s[A-Z]+\s[0-9a-z]+\s->\s[a-z]+$', line)


def is_not_action(line):
    return re.match('^NOT\s[a-z]+\s->\s[a-z]+$', line)


def is_wire_input(line):
    return re.match('^\d+\s->\s[a-z]+$', line)


def is_wire_assignment(line):
    return re.match('^[a-z]+\s->\s[a-z]+$', line)

input_text = get_input()

lines = {}

for line_input in input_text:
    wire_key = get_assigned_wire(line_input)
    lines[wire_key] = line_input

key = sys.argv[1]

print process_line(lines[key])
