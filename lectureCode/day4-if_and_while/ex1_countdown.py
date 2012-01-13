#!/usr/bin/env python

c = raw_input("Countdown from?  ")
c = int(c)

while c > 0:
    print "%d..." % c
    c -= 1

print "Blastoff!"
