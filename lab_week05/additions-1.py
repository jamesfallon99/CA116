#!/usr/bin/env python

i = 0
while i < 10:
    s = raw_input()
    j = 0
    while j < len(s) and s[j] != "+":
        j = j + 1
    print int(s[:j]) + int(s[j + 1:])
    i = i + 1
