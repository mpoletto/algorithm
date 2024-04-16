#!/usr/bin/python3

from collections import Counter
import sys
sys.set_int_max_str_digits(100000)

def fib(n, counter):
    count = 1
    i = 1 
    _sum = 1
    first = 1
    second = 1
    if n < 3:
        return 1
    while i <= n:
        counter.update({i: 1})
        _sum = first + second
        first = second
        second = _sum
        i += 1
        if i % 10 == 0:
            print(_sum)
    return _sum

if __name__ == "__main__":
    number = int(input())
    counter = Counter()
    print(fib(number, counter))
    print("%12s%15s" % (number, counter))
