from shared import *
import re

input_ary = read_input('input.txt')

def array_contains_abba(s_array):
    for s in s_array:
        if contains_abba(s):
            return True
    return False

def contains_abba(s):
    for i in range(0, len(s)-3):
        if (s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]):
            return True
    return False

total = 0
for line in input_ary:
    line = line.rstrip()
    m = re.finditer('(\[[a-z]+\])', line)
    s_array = [s.group(0) for s in m]
    if not array_contains_abba(s_array):
        split = re.split('\[[a-z]+\]', line)
        if array_contains_abba(split):
                total += 1

# print total
def has_converse(s):
    return s[0] == s[2]

def get_converse(s):
    return s[1]+s[0]+s[1]

def has_match(block_array, s_array):
    for block in block_array:
        for i in range(0, len(block)-3):
            sub_string = block[i:i+3]
            if has_converse(sub_string):
                converse = get_converse(sub_string)
                for s in s_array:
                    if converse in s:
                        return True
    return False

total = 0
for line in input_ary:
    line = line.rstrip()
    m = re.finditer('(\[[a-z]+\])', line)
    block_array = [s.group(0) for s in m]
    s_array = re.split('\[[a-z]+\]', line)
    if has_match(block_array, s_array):
        total += 1

print total