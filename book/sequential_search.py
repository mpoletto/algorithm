#!/usr/bin/python3

def sequentialSearch(target, lyst):
    position = 0
    while position < len(lyst):
        if lyst[position] == target:
            return position
        position += 1
    return -1

print(sequentialSearch(23, [10,8,6,23,58]))