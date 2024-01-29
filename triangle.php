<?php

/**
 * Author: Marcos Poletto Alves
 * Date: 2024-01-27
 */

function triangle($x) {

    // Define the first element. I'm supposing the triangle begin with it.
    $b[0][0] = 1;

    // loop through the cardinals until the number passed as argument
    for ($i=1; $i<=$x; $i++) {

        // Loop through the cardinals beginning with zero until argument.
        // Thus, we can use the left and right borders of the array to sum zero to them. 
        for ($j=0; $j<=$i; $j++) {

            // Test if values don't exist on the left and right could enable value changes to zero, 
            // keeping the entire logic of the triangle.
            $tmpa = !isset($b[$i-1][$j-1])? 0: $b[$i-1][$j-1];
            $tmpb = !isset($b[$i-1][$j])? 0: $b[$i-1][$j];
            $b[$i][$j] = (int)$tmpa + (int)$tmpb;

        }

    }

    return $b;

}

print_r(triangle(5));