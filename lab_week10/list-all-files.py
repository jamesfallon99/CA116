#!/usr/bin/env python

import os
ds = ["."]

while 0 < len(ds):
    d = ds.pop()
    entries = os.listdir(d)
    i = 0
    while i < len(entries):
        path = d + "/" + entries[i]
        if os.path.isfile(path):
            print path
        else:
            ds.append(path)
        i = i + 1
