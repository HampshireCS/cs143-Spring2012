#!/usr/bin/env python

people = {'Jonah' : "stupid",
       'Alec' : "ugly",
       'Jack' : "smelly",
       'Paul' : "awesome"}

name = raw_input("Your Name: ")

if name in people:
    print "%s is %s!" % (name, people[name])
else:
    print "I don't know %s." % name