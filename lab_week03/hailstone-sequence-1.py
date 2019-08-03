#!/usr/bin/env python

n = input()
m = input()
i = 0
while i < n:
    if m % 2 != 0:
        m = m * 3 + 1
    else:
        m % 2 == 0
        m = m / 2
    print m
    i = i + 1
