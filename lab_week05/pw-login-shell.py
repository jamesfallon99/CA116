#!/usr/bin/env python

s = raw_input()
while s != "end":
    i = 0
    while i < len(s) and s[len(s) - i - 1] != ":":
        i = i + 1
    if i < len(s):
        j = 0
    while j < len(s) and s[j] != ":":
        j = j + 1
    if j < len(s):
        print s[:j], s[(len(s) - i):]
    s = raw_input()
