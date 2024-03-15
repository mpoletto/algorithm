#!/usr/bin/python3

import math

lyst = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
def search(lst, n):

    left_lyst = []
    mid_nr = 0
    mid = 0
    right_lyst = []

    v = lst[math.floor(len(lst)/2)]
    if v < n:
        while v < n:
            tl = lst[lst.index(v):]
            v = tl[math.floor(len(tl)/2)]
            print(v)
    else:
        while v > n:
            tl = lst[:lst.index(v)]
            v = tl[math.floor(len(tl)/2)]
            print(v)

    mid = lst.index(v)
    mid_nr = lst[mid]

    for left in lst[:mid]:
        left_lyst.append(left)
    for right in lst[mid:]:
        right_lyst.append(right)
        

    return [left_lyst, mid_nr, right_lyst]

if __name__ == '__main__':
    n = int(input().strip())
    print(search(lyst, n))
