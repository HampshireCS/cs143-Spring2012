##!/usr/bin/env python
import sys

def main(args):
    "Average numbers"
    total = 0.0 # FLOAT THIS.
    for a in args:
        total += float(a)
    print "Avg: %s " % (total / len(args)) # %f works but is ugly, don't use %d !

if __name__ == '__main__':
    main(sys.argv[1:])