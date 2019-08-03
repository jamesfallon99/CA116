#!/usr/bin/env python

import sys
s = sys.stdin.read()
s = s.split()

a = {}

i = 0
while i < len(s):
    if s[i] not in a:
        a[s[i]] = "one"
        i = i + 1
    else:
        print "snap: " + s[i]
        i = len(s)
