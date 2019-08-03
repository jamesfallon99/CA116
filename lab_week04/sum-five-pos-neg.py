#!/usr/bin/env python

p_total = 0
n_total = 0
i = 0
while i < 5:
    n = input()
    if n > 0:
        p_total = p_total + n
    else:
        n_total = n_total + n
    i = i + 1
print n_total, p_total
