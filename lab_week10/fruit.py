#!/usr/bin/env python

import sys
s = sys.stdin.read().split()
fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}
i = 0
while i < len(s):
    if s[i] in fruit:
        print s[i]
    i = i + 1
