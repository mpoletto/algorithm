#!/usr/bin/python3

'''
Author: Cody AI
Date: 2024-01-29
Note: For the ask bellow, Cody wrote two routines. This one and other renamed 
as "triangle_memo_code_ai.py". 
/ask Is possible improve the function to be faster?

"Yes, there are a couple ways we could optimize the triangle function to improve its speed:

1. Use a formula to directly calculate triangle numbers instead of iteration:
 - The nth triangle number is n(n+1)/2
 - Can directly generate each row's elements with this formula
'''

import math

def triangle_code_ai(n):
  triangle = [[1]]
  for row in range(2, n+1):
    row = [math.comb(row-1, i) for i in range(row)]
    triangle.append(row)
  
  return triangle

print(triangle_code_ai(5))