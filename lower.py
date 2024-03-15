#!/usr/bin/python3

def displayRange(lower, upper):
    # while lower <= upper:
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)

def ourSum(lower, upper):
    if lower > upper:
        return 0
    else:
        res = lower + ourSum(lower + 1, upper)
        print(res)
        return res

print(ourSum(1, 5))