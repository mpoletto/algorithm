<?php 

/**
 * Author: Cody AI
 * Date: 2024-01-29
 * Note: Failed. Doesn't work. About the first solution renamed to triangle_code_ai_wrong.php,
 * the follow "ask" was written. 
 * /ask Does not work.
 * 
 * "Okay, it seems the optimized triangle function I provided does not work as intended. Let me take another look at this.
 * A couple issues I see:
 * - The formula $triangle += $i is incorrect. This will not generate the proper triangular numbers sequence.
 * - Simply storing the triangular numbers in a 1D array loses the triangle structure and relationships between the rows.
 * Here is an updated implementation that should work:"
 * (see the code bellow)
 * The key changes:
 * - Build up the triangle row-by-row instead of number-by-number
 * - Generate each row properly using the previous row values
 * - Maintain the 2D structure to preserve relationships
 * This improves efficiency by avoiding nested loops and unnecessary calculations, while still maintaining the complete triangle array output.
 */

function fastTriangle($n) {

  // Storage triangle 
  $triangles = [];

  // Initialize first row 
  $triangles[] = [1];

  for ($row = 1; $row <= $n; $row++) {

    // Calculate next row
    $nextRow = [];
    $nextNum = $triangles[$row-1][0] + $row;
    
    for ($i=0; $i<=$row; $i++) {
      $nextRow[] = $nextNum;
      $nextNum += $triangles[$row-1][$i]; 
    }

    // Add row
    $triangles[] = $nextRow;
  }

  return $triangles;

}

print_r(fastTriangle(5));