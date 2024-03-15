#!/usr/bin/python3

def sequentialSearch(target, lyst):
    
    middle = len(lyst)//2
    left_lyst = lyst[:middle]
    right_lyst = lyst[middle:]
    
    position = 0
    while position < len(left_lyst):
        if left_lyst[position] == target:
            return left_lyst[position]
        position += 1

    position = 0
    while position < len(right_lyst):
        if right_lyst[position] == target:
            return right_lyst[position]
        position += 1

    return -1

if __name__ == "__main__":
    import random
    lyst = []
    for i in range(100):
        n = random.randint(0,100)
        lyst.append(n)
    number = int(input())
    s = sequentialSearch(number, lyst)
    print(lyst[s], lyst)  