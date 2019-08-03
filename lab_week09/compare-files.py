#!/usr/bin/env python

import sys
f1 = sys.argv[1]
f2 = sys.argv[2]

with open(f1) as f:
    s = f.read()
with open(f2) as f:
    t = f.read()

i = 0
while i < len(s) and i < len(t) and s[i] == t[i]:
    i = i + 1

if i < len(s) or i < len(t):
    s = s[:i]
    lines = s.split("\n")
    print len(lines) - 1, len(lines[len(lines) - 1])
