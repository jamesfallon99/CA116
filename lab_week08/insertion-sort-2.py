#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
    a.append(int(s))
    s = raw_input()
n = input()
a.append(None)
j = len(a) - 1
while j > 0 and a[j - 1] > n:
    a[j] = a[j - 1]
    j = j - 1
a[j] = n
print a
