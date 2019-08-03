#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
    a.append(s)
    s = raw_input()
t = raw_input()
b = ""
while t != "end":
    if t.isdigit():
        if b:
            b += " "
        b += a[int(t)]
    else:
        print b
        b = ""
    t = raw_input()
if b:
    print b
