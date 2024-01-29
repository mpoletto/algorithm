#!/usr/bin/python3

'''
Author: Marcos Poletto Alves
Date: 2024-01-28
'''

def triangle(x):
    a = [[1]]
    for i in range(1, x+1):
        tmp = []
        for j in range(i):
            if j == 0:
                tl = 0 + a[i-1][j]
                tmp.append(tl)
            elif j < len(a[i-1]): 
                tm = a[i-1][j-1] + a[i-1][j]
                tmp.append(tm)
            
            if j == len(a[i-1])-1:
                tr = a[i-1][j] + 0
                tmp.append(tr)
        a.append(tmp)

    return a


print(triangle(10))