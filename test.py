#!/usr/bin/python3
import random

times = 5

for i in range(times):
    print(i*0.6)

print("list size: ")
lyst = [1,2,3,2]
print(len(lyst))

print("list index: ")
print(lyst.index(2))

lyst.pop(1)
print(lyst)

lyst[1] = 2
print(lyst)


# generate random number list and print it
print("Random list: ")
x = random.sample(range(100), 10)
print(x)

print("for: ")
for x in range(2,5):
    print(x)