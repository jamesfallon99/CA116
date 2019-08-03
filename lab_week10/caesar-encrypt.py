#!/usr/bin/env python

import sys
s = sys.stdin.read().strip()

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

d = {}
i = 0
while i < len(src):
    d[src[i]] = dst[i]
    i = i + 1

t = []
j = 0
while j < len(s):
    if s[j] not in src:
        t.append(s[j])
    else:
        t.append(d[s[j]])
    j = j + 1
print "".join(t)
