#!/usr/bin/python3

from collections import Counter
import sys
sys.set_int_max_str_digits(100000)

def fib(n):
    count = 1
    _sum = 1
    first = 1
    second = 1
    if n < 3:
        return 1
    while count <= n:
        _sum = first + second
        first = second
        second = _sum
        count += 1
        if count % 10 == 0:
            print(_sum, count)
    return _sum

if __name__ == "__main__":
    number = int(input())
    print(fib(number))
