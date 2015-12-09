import re


def get_input():
    with open('input.txt') as f:
        return f.readlines()


# part 1 functions
def contains_at_least_three_vowels(string):
    matches = re.findall("([aeiou])", string)
    if len(matches) > 2:
        return True
    return False


def contains_repeating_letters(string):
    matches = re.findall("(\w)\\1+", string)
    if len(matches) > 0:
        return True
    return False


def does_not_contain_bad_chars(string):
    matches = re.findall("(ab)|(cd)|(pq)|(xy)", string)
    if len(matches) > 0:
        return False
    return True


# part 2 functions
def repeating_pairs(string):
    matches = re.findall('(\w{2}).*\\1', string)
    if len(matches) > 0:
        return True
    return False


def letter_in_middle(string):
    matches = re.findall("(\w)\w\\1", string)
    if len(matches) > 0:
        return True
    return False


def part_two():
    text = get_input()
    test_text = [
        'qjhvhtzxzqqjkmpb',
        'xxyxx',
        'uurcxstgmygtbstg',
        'ieodomkazucvgmuy'
    ]
    count = 0
    for line in text:
        print line
        print repeating_pairs(line)
        print letter_in_middle(line)

        if letter_in_middle(line) and repeating_pairs(line):
            count += 1
        print count


def part_one():
    text = get_input()
    test_text = [
        'ugknbfddgicrmopn',
        'aaa',
        'jchzalrnumimnmhp',
        'haegwjzuvuyypxyu',
        'dvszwmarrgswjxmb'
    ]
    count = 0
    for line in text:
        print line
        print contains_at_least_three_vowels(line)
        print contains_repeating_letters(line)
        print does_not_contain_bad_chars(line)

        if contains_at_least_three_vowels(line) and contains_repeating_letters(line) and does_not_contain_bad_chars(line):
            count += 1
        print count


# part_one()
part_two()
