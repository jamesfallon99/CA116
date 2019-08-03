#!/usr/bin/env python

p_total = 0
n_total = 0
n = input()
while n != 0:
    if n > 0:
        p_total = p_total + n
    else:
        n_total = n_total + n
    n = input()
print n_total, p_total
