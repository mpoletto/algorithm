#!/usr/bin/python3

def factorial(n, product = 1):
    if n == 1:
        return product
    else:
        x = factorial(n - 1, n * product)
        print(n, product)
        return x
    
print(factorial(5))