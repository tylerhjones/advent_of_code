from shared import *
import re
from collections import OrderedDict


input_ary = read_input('input.txt')

total = 0

def compare(a,b):
    if a[1] == b[1]:
        if a[0] < b[0]:
            return 1
        else:
            return -1
    else:
        if a[1] > b[1]:
            return 1
        else:
            return -1

def new_char(c, rotation):
    if c == '-':
        return ' '
    cipher_from = {}
    cipher_to = {}
    for i in range(1, 27):
        cipher_to[i] = chr(96+i)
        cipher_from[96+i] = i

    index = (cipher_from[ord(c)] + rotation) % 26

    if index == 0:
        index += 1
    return cipher_to[index]

part2 = []

for line in input_ary:
    line = line.rstrip()
    m = re.search('\[(\w+)\]', line)
    check_sum = m.group(1)

    m = re.search('(\d+)\[', line)
    sector_id = m.group(1)

    m = re.search('^(.+)-\d+\[\w+\]$', line)
    name = m.group(1)

    withoutDash = ''.join(sorted(name.replace('-','')))
    d ={}
    for c in withoutDash:
        d[c] = name.count(c)

    a = []
    for key in d:
        a.append((key, d[key]))

    sort_a = sorted(a, cmp=compare, reverse=True)

    s = ''
    for t in sort_a:
        s+=t[0]

    if (check_sum in s):
        total += int(sector_id)

    decrypted_name = ''
    for c in name:
        decrypted_name += new_char(c, int(sector_id))
        if decrypted_name == 'northpole object storage':
            print decrypted_name
            print sector_id

# print "Part 1:"
# print total
