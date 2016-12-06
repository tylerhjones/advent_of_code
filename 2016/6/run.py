from shared import *
import string

input_ary = read_input('input.txt')

key = []
for i in range(0, len(input_ary[0].rstrip())):
    key.append({})

for i in range(0, len(key)):
    for x in string.ascii_lowercase:
        key[i][x] = 0

print key

for line in input_ary:
    s = line.rstrip()
    for i in range(0,len(s)):
        key[i][s[i]] +=1

t = ''
for c in key:
    print c
    # t+=max(c, key=lambda key: c[key])
    t+=min(c, key=lambda key: c[key])
print t