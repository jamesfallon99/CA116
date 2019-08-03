#!/usr/bin/env python

import sys
total = 0
i = 1
while i < len(sys.argv):
    s = sys.argv[i]
    with open(s) as f:
        s = f.readline()
        while 0 < len(s):
            total = total + int(s)
            s = f.readline()
    i = i + 1
print total
