#!/usr/bin/env python
import sys

last = None

def print_coordinates(x, values):
    for i, value in enumerate(values):
        print "%f %f %f" % (x, i, float(value))
        print "%f %f %f" % (x, i + 1, float(value))
    print

for line in sys.stdin.readlines():
    items = line.rstrip().split(',')
    current = items[1:]
    x = float(items[0])

    if last:
        print_coordinates(x, last)

    print_coordinates(x, current)
    last = current
