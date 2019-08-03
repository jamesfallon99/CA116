#!/usr/bin/env python

s = raw_input()
t = raw_input()
a = []
while s != "end":
    a.append(int(s))
    s = raw_input()
n = []
while t != "end":
    n.append(int(t))
    t = raw_input()

c = a + n

i = 0
while i < len(c):
    p = i
    j = i + 1
    while j < len(c):
        if c[j] < c[p]:
            p = j
        j = j + 1
    tmp = c[p]
    c[p] = c[i]
    c[i] = tmp
    i = i + 1
k = 0
while k < len(c):
    print c[k]
    k = k + 1
