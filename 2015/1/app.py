import sys

def get_input():
    with open('input.txt') as f:
        return f.readlines()[0]

def get_value(char):
    if char == '(':
        return 1
    if char == ')':
        return -1
    if char == '\n':
        return 0
    raise Exception("Could not parse [%s]" % char)

input = get_input()

total = 0
for index, character in enumerate(input):
    total += get_value(character)
    if total == -1:
        print index
        print total
        sys.exit(0)
