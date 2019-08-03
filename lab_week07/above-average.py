#!/usr/bin/env python

s = raw_input()
a = []
total = 0
while s != "end":
    a.append(int(s))
    s = raw_input()
i = 0
while i < len(a):
    total = total + a[i]
    i = i + 1
j = 0
while j < len(a):
    if a[j] > total / len(a):
        print a[j]
    j = j + 1
