#!/usr/bin/env python

def input_nums(msg="Enter some numbers, seperated by ',':  "):
    inp = raw_input(msg).strip()
    return [ int(c.strip()) for c in inp.split(",") ]

