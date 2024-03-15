#!/usr/bin/python3

def multiply(r0, r1):
    assert r0 >= 0 and r1 >= 0
    result = 0
    while r1 > 0:
        r1 -= 1
        result += r0
    return result

assert multiply(4, 5) == 20
assert multiply(40, 3) == 120

def multiple(a, b):
    assert a >= 0 and b >= 0
    if a == 1:
        return b
    else:
        return b + multiple(a - 1, b)

# print(multiple(4, 5))
assert multiple(4, 5) == 20
assert multiple(40, 3) == 120
    