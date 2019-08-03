#!/usr/bin/env python

n = input()
i = 0
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print "fizz-buzz"
    elif i % 3 == 0:
        print "fizz"
    elif i % 5 == 0:
        print "buzz"
    else:
        print i
    i = i + 1
