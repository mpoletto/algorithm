#!/usr/bin/python3
'''
https://www.bigscal.com/blogs/backend/binary-search-its-use-cases-and-complexities/
ou eu sou louco ou esse código está errado, ele não retorna o que propõe, ele retorna 
o que está impresso, ou seja, ele retorna algo errado que foi dado como certo
'''
def getMax(lyst, length):
    low = 0
    high = length - 1
    while (low <= high):
        mid = low + (high - low) # 2 - Find the value of mid
        print(low, mid, high)
        if (lyst[mid] < 0): # If element is negative then, ignore the left half
            low = mid + 1
        elif (lyst[mid] > 0): # If element is positive then, ignore the right half
            high = mid - 1
        
    return max(low, length - low) # Return maximum among the count of positive & negative element

if __name__ == "__main__":
    lyst = [-19, -12, -7, -5, -1, 8, 12]
    n = len(lyst)
    print(getMax(lyst, n))