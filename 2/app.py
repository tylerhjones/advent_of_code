def get_input():
    with open('input.txt') as f:
        return f.readlines()

def get_paper_needed(l,w,h):
    x = [l*w, w*h, h*l]
    return (2*sum(x)) + min(x) # the min is the smallest side

def get_ribbon_needed(l,w,h):
    bow_length = l*w*h
    x = [(2*l)+(2*w), (2*l)+(2*h), (2*h)+(2*w)]
    return min(x) + bow_length

lines = get_input()

total_paper = 0
total_ribbon = 0

for line in lines:
    x = line.split('x')
    length = int(x[0])
    width = int(x[1])
    height = int(x[2])

    total_paper += get_paper_needed(length, width, height)
    total_ribbon += get_ribbon_needed(length, width, height)

print "Paper: %s" % total_paper
print "Ribbon: %s" % total_ribbon
