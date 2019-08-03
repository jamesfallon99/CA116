#!/usr/bin/env python

import sys
s = sys.stdin.read().split()

db = {}
dg = {}
either = {}

i = 0
with open("boys.txt", "r") as f:
    b = f.read().split()
    while i < len(b):
        boy_name = b[i]
        if boy_name not in db:
            db[boy_name] = "boy"
        i = i + 1


j = 0
with open("girls.txt", "r") as f:
    g = f.read().split()
    while j < len(g):
        girl_name = g[j]
        if girl_name not in dg:
            dg[girl_name] = "girl"
        j = j + 1

n = 0
while n < len(g):
    either_bg = g[n]
    if either_bg in db and either_bg in dg:
        either[either_bg] = "either"
    n = n + 1

i = 0
while i < len(s):
    if s[i] in either:
        print s[i], either[s[i]]
        i = i + 1
    elif s[i] in db:
        print s[i], db[boy_name]
        i = i + 1
    elif s[i] in dg:
        print s[i], dg[girl_name]
        i = i + 1
