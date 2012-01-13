#!/usr/bin/env python

print "Let's add up a bunch of numbers"
print "Enter some numbers (or nothing to stop) "

total = 0
output = ""
inp = raw_input("> ")
while inp != "":
    # parse the int
    inp = int(inp)
    total += inp

    # append input to output string
    if output != "" and inp < 0:
        output += " - %d" % abs(inp)
    elif output != "":
        output += " + %d" % inp
    else:
        output = str(inp)
        
    # print
    print output, "=", total
    
    # get next number
    inp = raw_input("> ")
