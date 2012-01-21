#!/usr/bin/env python
"ex3_insult.py"

TAs = ["Alec","Jack","Jonah"]

inp = raw_input("Enter your name:  ")

if inp == "Paul":
    print "you are cool"
elif inp in TAs:
    print "you smell bad"
else:
    print "you need some learnin'"
