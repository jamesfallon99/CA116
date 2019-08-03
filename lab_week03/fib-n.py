#!/usr/bin/env python

n = input()
i = 0
prev = 0
curr = 1
while i < n:
    old_curr = curr
    curr = prev + curr
    prev = old_curr
    print prev
    i = i + 1
