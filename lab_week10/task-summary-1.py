#!/usr/bin/env python

import sys
s = sys.stdin.readline().strip()
d = {}
while len(s) != 0:
    d[".".join(s.split(".")[0:2])] = s.split(".")[2]
    s = sys.stdin.readline().strip()
for file in d:
    if d[file] == "correct":
        print file
