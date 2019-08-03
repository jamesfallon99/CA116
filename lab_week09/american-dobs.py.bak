#!/usr/bin/env python

with open("irish-dobs.txt") as f:
    a = f.readlines()

with open("american-dobs.txt", "w") as f:
    i = 0
    while i < len(a):
        tokens = a[i].split("/")
        f.write(tokens[1] + "/" + tokens[0] + "/" + tokens[2])
        i = i + 1
