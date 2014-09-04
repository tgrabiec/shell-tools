#!/usr/bin/env python
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument("-s", "--step", action="store", 
                        help="Bucket size")
    args = parser.parse_args()

    level = 0
    count = 0
    cumul = 0
    prev_value = None

    def print_line():
        print '%7f %10d %10.2f' % (level, count, cumul)

    for line in sys.stdin:
        value = float(line)
        if prev_value != None and value < prev_value:
            raise Exception('Input not sorted!')

        while value > level:
            print_line()
            level += float(args.step)
            count = 0

        count += 1
        cumul += value

        prev_value = value

    if count:
        print_line()
