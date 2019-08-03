#!/usr/bin/env python

import sys

pages = []

i = 0
while i < 10:
    name = "page-" + str(i) + ".txt"
    with open(name) as f:
        pages.append(f.readlines())
    i = i + 1

triplets = sys.stdin.readlines()

i = 0
while i < len(triplets):
    triplet = triplets[i].split()
    page = int(triplet[0])
    line = int(triplet[1])
    char = int(triplet[2])
    ch = pages[page][line][char]
    sys.stdout.write(ch)
    i = i + 1
