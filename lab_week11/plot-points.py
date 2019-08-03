#!/usr/bin/env python

import sys
n = 20

plot = {}

lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    line = lines[i]
    tokens = line.split()
    key = tokens[0] + "-" + tokens[1]
    plot[key] = True
    i = i + 1

def should_plot(x, y):
    key = str(x) + "-" + str(y)
    return key in plot

print " " + "-" * n
i = 0
while i < n:
    y = n - i - 1
    output = []
    x = 0
    while x < n:
        if should_plot(x, y):
            output.append("*")
        else:
            output.append(" ")
        x = x + 1
    print "|" + "".join(output) + "|"
    i = i + 1
print " " + "-" * n
