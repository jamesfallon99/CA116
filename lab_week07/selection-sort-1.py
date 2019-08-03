#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
    a.append(int(s))
    s = raw_input()
j = 0
i = 1
while i < len(a):
    if a[i] < a[j]:
        j = i
    i = i + 1
print j
