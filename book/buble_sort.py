#!/usr/bin/python3

from util import swap

def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
            i += 1
        n -= 1
    return lyst

lyst = [5, 7, 89, 5, 12, 5, 10, 32, 5, 89]
print(bubbleSort(lyst))