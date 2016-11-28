from ast import literal_eval
import re


def get_input():
    with open('input.txt') as f:
        return f.readlines()


def get_code_count(line):
    return len(line.rstrip())


def get_mem_count(line):
    e = literal_eval(line.rstrip())
    return len(e)


def get_escape_count(line):
    e = re.escape(line.rstrip())
    return len(e) + 2

input_lines = get_input()

code_total = 0
mem_total = 0
esc_total = 0

for line in input_lines:
    code_total += get_code_count(line)
    mem_total += get_mem_count(line)
    esc_total += get_escape_count(line)

print code_total
print mem_total
print code_total - mem_total
print esc_total - code_total