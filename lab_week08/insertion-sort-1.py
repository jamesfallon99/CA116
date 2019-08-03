#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
    a.append(int(s))
    s = raw_input()
n = input()
i = len(a)
while i > 0 and a[i - 1] > n:
    i = i - 1
print i
