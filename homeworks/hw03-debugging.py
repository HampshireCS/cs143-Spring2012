#!/usr/bin/env python

from hwtools import input_nums

Section 1:  What Does This Code Do?
=====================================

## question 1
a = input_nums()
b = None
for c in a:
    if b is None or c >= b:
        b = c
print b
## end of question 1
print "Question 1: _______"



## question 2

## end of question 2
print "Question 2: _______"



## question 3
t1 = []
t2 = []
while len(t1) != 2:
    t1 = input_nums()
while len(t2) != 2:
    t2 = input_nums()
print t2[1]-t1[1]/float(t2[0]-t1[0])
## end of question 3
print "Question 3: _______"



Section 2:  What Should This Code Do?



Section 3:  Fix This Code
