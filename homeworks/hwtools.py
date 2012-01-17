#!/usr/bin/env python

def input_nums():
    inp = raw_input("Enter some numbers, separated by ',':  ").strip()
    return [ int(c.strip()) for c in inp.split(",") ]

