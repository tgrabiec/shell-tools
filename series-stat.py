#!/usr/bin/env python
import numpy
import sys

if __name__ == "__main__":
    values = list()
    for line in sys.stdin.readlines():
        values.append(float(line))
    if not values:
        print "No data"
    else:
        print "avg = %.2f" % numpy.mean(values)
        print "stdev = %.2f" % numpy.std(values)
        print "sum = %.2f" % sum(values)
        print "samples = %d" % len(values)
