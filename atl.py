#!/usr/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

def processLogs(logs, threshold):
    # Write your code here
    a, b = (None, None)
    count_a = 1
    count_b = 1
    result = []
    for _ in range(len(logs)):
        t = logs[_].split(' ')
        if a:
            if a in ([t[0], t[1]]):
                count_a += 1
        if b:
            if b in ([t[0], t[1]]):
                count_b += 1
        a, b = t[0], t[1]
    if count_a >= threshold:
        result.append(a)
    if count_b >= threshold:
        result.append(b)

    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())

    result = processLogs(logs, threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()