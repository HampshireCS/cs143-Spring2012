#!/usr/bin/env python
"ex1_countdown.py"

c = 0
while c <= 0:
    c = raw_input("Countdown from?  ")
    c = int(c)

while c > 0:
    print "%d..." % c
    c -= 1

print "Blastoff!"
