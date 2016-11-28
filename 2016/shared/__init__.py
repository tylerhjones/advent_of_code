import sys

def read_input(fname):
    with open(fname) as f:
        content = f.readlines()
        return content