#!/usr/bin/env python

s = raw_input()
t = raw_input()
u = raw_input()
if len(s) > len(t) and len(s) > len(u):
    print s
elif len(s) < len(t) and len(u) < len(t):
    print t
elif len(s) < len(u) and len(t) < len(u):
    print u
