#!/usr/bin/env python

n = raw_input("Enter a number:  ")
m = raw_input("Enter another:  ")

n = int(n)
m = int(m)

print "%d+%d=%d" % (n,m,n+m)
print "%d-%d=%d" % (n,m,n-m)
print "%d*%d=%d" % (n,m,n*m)
print "%d/%d=%f" % (n,m,n/float(m))
