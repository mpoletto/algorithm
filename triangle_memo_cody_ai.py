#!/usr/bin/python3

'''
Author: Cody AI
Date: 2024-01-29
Note: For the ask bellow, Cody wrote two routines. This one and other renamed as "triangle_code_ai.py". 
/ask Is possible improve the function to be faster?

"Yes, there are a couple ways we could optimize the triangle function to improve its speed:

1. Use dynamic programming with memoization:
 - Store previously computed triangle rows in a memo dictionary
 - Before computing a new row, check if it's already in the memo and return that instead of recomputing
 - Store the final memo dictionary returned instead of creating a new triangle list each time"
'''

def triangle_memo_cody_ai(n):
  memo = {1: [[1]]}

  def compute_row(row):
    if row in memo:
      return memo[row]
    
    prev_row = memo[row-1]
    new_row = [1]
    
    for i in range(len(prev_row)-1):
      new_row.append(prev_row[i] + prev_row[i+1])
    
    new_row.append(1)
    memo[row] = new_row
    return new_row

  for row in range(2, n+1):
    compute_row(row)

  return memo

print(triangle_memo_cody_ai(5))