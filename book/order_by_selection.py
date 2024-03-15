#!/usr/bin/python3

from util import swap

def orderList(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            print(i, j)
            if lyst[j] < lyst[minIndex]:
                print(lyst[j], lyst[i], j, minIndex)
                minIndex = j
            j += 1
        print("---")
        # print(lyst)
        if minIndex != i:
            swap(lyst, minIndex, i)
        # print(lyst)
        # print("--------")
        i += 1
    return lyst

# print("Number of lyst's element: ")
# numbers = int(input().strip())
# print(numbers, "elements' lyst: ")
# lyst = []
# for _ in range(numbers):
#     lyst.append(input())
# print(lyst)
lyst = [5,7,89,5,12,5,10,32,5,89]
print(lyst)
print(orderList(lyst))