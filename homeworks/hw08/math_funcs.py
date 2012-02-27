#!/usr/bin/env python

import math

def distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1]-a[1])**2)

def normalize(vec):
    if not any(vec):
        return vec

    total = 0
    for v in vec:
        total += v**2
    length = math.sqrt(total)
    
    return [ v/length for v in vec ]
