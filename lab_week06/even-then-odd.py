#!/usr/bin/env python

odds = []
s = raw_input()
while s != "end":
    n = int(s)
    if n % 2 == 0:
        print n
    else:
        odds.append(n)
    s = raw_input()
i = 0
while i < len(odds):
    print odds[i]
    i = i + 1
