#!/usr/bin/env python
import subprocess
import sys

if __name__ == "__main__":
    command = 'plot ' + ', '.join('\"%s\" w lines' % file for file in sys.argv[1:])
    print command
    subprocess.call(['gnuplot', '-p', '-e', command])
