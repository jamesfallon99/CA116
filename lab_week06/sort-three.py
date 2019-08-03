#!/usr/bin/env python

n = input()
m = input()
r = input()

if n < m and n < r:
    print n
    if r < m:
        print r
        print m
    else:
        print m
        print r
elif m < n and m < r:
    print m
    if r < n:
        print r
        print n
    else:
        print n
        print r
else:
    print r
    if m < n:
        print m
        print n
    else:
        print n
        print m
