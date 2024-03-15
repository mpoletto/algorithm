#!/usr/bin/python3

import math
import random

def indexOfMin(lyst):

    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return lyst[minIndex]

for x in range(10):
    lyst = []
    for i in range(10):
        n = random.randrange(1,1000)
        lyst.append(n)
    print(lyst)
    print(indexOfMin(lyst))
    print("-------------------")
