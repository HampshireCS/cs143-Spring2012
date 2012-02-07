#!/usr/bin/env python

def answer(val):
    print "Answer is: %r" % val

def get():
    return None

## initialize magic builtins
import  __builtin__
from functools import partial

def_builtin = partial(setattr, __builtin__)

def_builtin("__", "FILL_ME_IN")
def_builtin("answer", answer)
def_builtin("get", get)
### definitions for the actual assignment

