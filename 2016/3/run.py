from shared import *
import re


input_ary = read_input('input.txt')

count = 0

def is_triangle(arr):
    largest = max(numbers)
    numbers.pop(numbers.index(largest))

    return largest < (numbers[0] + numbers[1])

for line in input_ary:
    matches = re.findall('(\d{1,3})', line)
    numbers = [int(x) for x in matches]

    if is_triangle(numbers):
        count += 1

print count

count = 0

for i in range(1, len(input_ary), 3):
    matches1 = re.findall('(\d{1,3})', input_ary[i-1])
    matches2 = re.findall('(\d{1,3})', input_ary[i])
    matches3 = re.findall('(\d{1,3})', input_ary[i+1])

    set = [[matches1[0], matches2[0], matches3[0]],
     [matches1[1], matches2[1], matches3[1]],
     [matches1[2], matches2[2], matches3[2]]]

    for m in set:
        numbers = [int(x) for x in m]
        if is_triangle(numbers):
            count += 1

print count

