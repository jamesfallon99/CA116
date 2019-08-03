#!/usr/bin/env python

s = raw_input()
while s != "1000":
    j = 0
    while j < len(s) and s[j] != "+":
        j = j + 1
    print int(s[:j]) + int(s[j + 1:])
    s = raw_input()
