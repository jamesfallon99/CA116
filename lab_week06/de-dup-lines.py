#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
    i = 0
    while i < len(a) and a[i] != s:
        i = i + 1

    if not i < len(a):
            a.append(s)
    s = raw_input()
i = 0
while i < len(a):
    print a[i]
    i = i + 1
