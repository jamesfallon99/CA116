#!/usr/bin/env python

import sys
file_name = sys.argv[1]
words = sys.argv[2:]
with open(file_name, "w") as f:
    i = 0
    while i < len(words):
        f.write(words[i] + "\n")
        i = i + 1
