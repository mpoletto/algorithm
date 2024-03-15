#!/usr/bin/python3

from collections import Counter

def fib(n, counter):
    counter.update({count: 1})
    if n < 3:
        return 1
    else:
        return fib(n - 1, counter) + fib(n - 2, counter)
    
problemSize = 32
print("%12s%15s" % ("Problem Size", "Calls"))
for count in range(5):
    counter = Counter()
    fib(problemSize, counter)
print("%12d%15s" % (problemSize, counter))