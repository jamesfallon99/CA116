#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
    a.append(int(s))
    s = raw_input()
i = 0
while i < len(a):
    v = a[i]
    p = i
    while p > 0 and a[p - 1] > v:
        a[p] = a[p - 1]
        p = p - 1
    a[p] = v
    i = i + 1
j = 0
while j < len(a):
    print a[j]
    j = j + 1
