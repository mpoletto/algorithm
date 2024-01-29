<?php
/**
 * Author: Cody AI
 * Date: 2024-01-29
 * Note: Failed. Doesn't work. 
 * /ask is possible improve the function to be faster?
 * 
 * "Here are some ways the triangle function could be optimized to improve performance:
 * 1. Cache repeated calculations:
 * The $tmpa and $tmpb variables are recalculated in each iteration of the inner loop. We could cache these outside the inner loop to avoid repeating the isset() and array access calculations.
 * 1. Remove unnecessary type casting:
 * The (int) type casts on $tmpa and $tmpb are redundant since the values are already integers. Removing these would avoid unnecessary operations.
 * 1. Use memoization:
 * The function calculates the same triangular numbers over and over. We could memoize previously computed triangles in a cache and return those instead of recalculating.
 * 1. Use more efficient data structures:
 * The 2D array for storing the triangle is convenient but inefficient for incremental building. A 1D array that maps indices to values could be faster.
 * 1. Optimize algorithm complexity:
 * The nested loops lead to O(N^2) complexity. There are O(N) algorithms for generating triangular numbers that would be faster for large inputs.
 * 1. Lower memory usage:
 * The full triangle array consumes a lot of memory. Storing only the current row instead of the full triangle could reduce memory usage.
 * 1. Parallelize computations:
 * The rows can be computed independently in parallel to take advantage of multiple CPU cores for speedup.
 * So in summary, caching, removing excess operations, memoization, data structure optimization, algorithm changes, reducing memory usage, and parallelism could all potentially improve the performance of the function. The optimal changes would depend on the specific use case and performance requirements.

 * 
 * Generate triangular numbers up to n efficiently"
 * 
 * When informed that it wasn't worked, Code AI generate a new routine renamed to triangle_code_ai_new_wrong.php
 * 
 * @param int $n Max number 
 * @return array Triangular numbers
*/
function fastTriangle($n) {

  // Storage for triangular numbers
  $triangles = [];

  // Formula for triangular number
  $triangle = 0;

  // Loop just up to n
  for ($i = 1; $i <= $n; $i++) {

    // Calculate next triangle number
    $triangle += $i;

    // Add to array
    $triangles[] = $triangle; 
  }

  return $triangles;

}

print_r(fastTriangle(5));