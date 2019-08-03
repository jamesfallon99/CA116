#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
    a.append(s)
    s = raw_input()
t = raw_input()
b = []
while t != "end":
    b.append(int(t))
    t = raw_input()
i = 0
j = 0
while i < len(a):
    while j < len(b) and a[i] != b[j]:
        print a[b[j]]
        j = j + 1
    i = i + 1
