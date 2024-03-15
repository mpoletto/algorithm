#!/usr/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

'''
first input line is the number of operations
1 = push element
2 = delete element (top on the stack)
3 = print the maximum element
Sample Input
----------------
STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output
26
91
'''

def getMax(operations):
    # Write your code here
    res = []
    for i in range(len(operations)):
        tmp = operations[i].split(' ')
        if int(tmp[0]) == 1:
            res.append(int(tmp[1]))
        elif int(tmp[0]) == 2:
            res.pop()
        else:
            print(max(res))
    print(res)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
