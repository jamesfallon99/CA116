#!/usr/bin/env python

import sys

cypher = {}
i = 0
while i < 10:
    name = "page-" + str(i) + ".txt"
    with open(name) as f:
        page = f.readlines()
    j = 0
    while j < len(page):
        line = page[j]
        k = 0
        while k < len(line):
            ch = line[k]
            triplet = str(i) + " " + str(j) + " " + str(k)
            if ch not in cypher:
                cypher[ch] = []
            cypher[ch].append(triplet)
            k = k + 1
        j = j + 1
    i = i + 1

text = sys.stdin.read()
i = 0
while i < len(text):
    print cypher[text[i]].pop()
    i = i + 1
