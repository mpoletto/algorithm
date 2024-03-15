#!/usr/bin/python3

def orderedBinarySearch(target, lyst):
    
    middle = len(lyst)//2
    
    if target == lyst[middle]:
        return lyst[middle]
    elif target < lyst[middle]:
        return orderedBinarySearch(target, lyst[:middle])
    elif target > lyst[middle]:
        return orderedBinarySearch(target, lyst[middle:])
    else:
        return -1

lyst = [0,2,3,6,8,10,23,54,58,77,85,98,124,457]
target = int(input(""))
result = orderedBinarySearch(target, lyst)
print(result, target, lyst)