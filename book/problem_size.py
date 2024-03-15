#!/usr/bin/python3

import time
from collections import Counter

# def problem_size(problemSize):
#     counter.update({count: 1})
#     work = 1
#     while problemSize > 0:
#         # print(problemSize)
#         work += 1
#         work -= 1
#         print(problemSize)
#         problemSize = problemSize // 2

# problemSize = 1000000
# print("%12s%15s" % ("Problem Size", "Calls"))
# for count in range(3):
#     start = time.process_time()
#     counter = Counter()
#     problem_size(problemSize)
#     elapsed = time.process_time() - start
# print("%12d%16.3f%15s" % (problemSize, elapsed, counter))

# from book resolution
problemSize = int(input("Enter the problem size: "))
count = 0
while problemSize > 0:
    problemSize = problemSize / 2
    count += 1
print(count)
