#!/usr/bin/env python

counts = []

i = 0
while i < 10:
    counts.append(0)
    i = i + 1
s = raw_input()
while s != "end":
    d = int(s)
    counts[d] = counts[d] + 1
    s = raw_input()
i = 0
while i < 10:
    print i, "*" * counts[i]
    i = i + 1
