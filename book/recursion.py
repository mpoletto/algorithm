#!/usr/bin/python3

def countdown(n):
    if n <= 0:
        print("LIFTOFF!")
    else:
        print(n)
        countdown(n - 1)

def sum_recursive(n):
    assert n >= 0
    if n < 1:
        return 0
    return n + sum_recursive(n - 1)

# countdown(10)
assert sum_recursive(10) == 55
assert sum_recursive(5) == 15 