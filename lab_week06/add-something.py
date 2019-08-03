#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
    a.append(s)
    s = raw_input()
n = input()

i = 0
while i < len(a):
    print n + int(a[i])
    i = i + 1
