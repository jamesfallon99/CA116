#!/usr/bin/env python

#!/usr/bin/env python

if __name__ == "__main__":
    a = ["dog", "", "cat", "", "mouse"]

count = 0
i = 0
while i < len(a):
    if a[i] != "":
        count = count + 1
    i = i + 1
print count
