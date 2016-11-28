import hashlib
import sys


def make_hash(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()

my_key = 'yzbqklnj'

i = 0
while True:
    s = make_hash(my_key + str(i))
    if s.startswith('000000'):
        print str(i)
        sys.exit(0)
    i+=1