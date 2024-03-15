#!/usr/bin/python3

from util import pushItem

def insertionSort(lyst):
    """
    See page 68 to an example of insertion
    """
    i = 0
    while i < len(lyst) - 1:
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[i]:
                # print(lyst[j], lyst[i])
                pushItem(lyst, i, j)
            j += 1
        i += 1
    return lyst

def bookInsertionSort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        print("j: ", j)
        while j >= 0:
            if itemToInsert < lyst[j]:
                print(lyst[j], j)
                lyst[j + 1] = lyst[j]
                j -= 1
                print(j, lyst)
            else:
                print(j)
                break
        lyst[j + 1] = itemToInsert
        i += 1
    return lyst

lyst = [5, 3, 89, 5, 12, 5, 10, 32, 5, 89]
# lyst = [5, 3, 5, 5, 5, 10, 12, 32, 89, 89]
print(lyst)
# print(insertionSort(lyst))
print(bookInsertionSort(lyst))