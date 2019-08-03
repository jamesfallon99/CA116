#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files):
    l = files[i].split(".")
    with open(files[i]) as f:
        s = f.readline()
        if s != "":
            if l[len(l) - 1] == "py":
                print files[i]
    i = i + 1
