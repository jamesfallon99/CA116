#! usr/bin/env python

n = input()
i = 0
while i < n:
    if n % 3 == 0:
        print "fizz"
    elif n % 5 == 0:
        print "buzz"
    elif n % 3 == 0 and n % 5 == 0:
        print "fizz-buzz"
    else:
        print n
    print n + i
    i = i + 1
