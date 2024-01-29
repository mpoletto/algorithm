<?php

/**
 * Author: Cody AI
 * Date: 2024-01-29
 * Note: Now it's working, after asked Cody again.
 * /ask the new php code you proposed does not work too.
 * 
 * The key issues in the previous code were:

 * - The loop conditions were off - should loop from 1 to < n, not <= n
 * - The next number calculation was incorrect
 * - Needed to append 1 to beginning and end of each row
 */

function generatePascalTriangle($n) {

    // Storage triangle 
  $triangles = [];

  // Initialize first row 
  $triangles[] = [1];

  for ($row = 1; $row <= $n; $row++) {
        // Calculate next row
        $nextRow = [];
        $nextRow[] = 1;

        for ($i = 1; $i < $row; $i++) {
            $nextRow[] = $triangles[$row-1][$i-1] + $triangles[$row-1][$i];
        }

        $nextRow[] = 1;

        // Add row
        $triangles[] = $nextRow;
    }

    return $triangles;
}


print_r(generatePascalTriangle(5));