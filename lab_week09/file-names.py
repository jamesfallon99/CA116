#!/usr/bin/env python

import sys
s = sys.stdin.readline()
a = []
i = 0
while i < len(s):
    a = (s.split("/"))
    a = a[len(a) - 1].split()
    print a[0]
    s = sys.stdin.readline()
    i = i + 1
