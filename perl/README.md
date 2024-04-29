# Algorithms from:  

https://staff.washington.edu/jon/dsa-perl/dsa-perl.html

# Case study: Maximum section sum  


## What is the difference if the result is the same?  

The bentley1.pl, bentley2.pl and bentley4.pl are algorithms that have the same functionality, which is to find the maximum subarray sum of a given array. However, the implementation and approach used in each algorithm differ:

### bentley1.pl cubic

"As a cubic algorithm, it begins by considering all possible subarrays and calculating the sum of each one. This is done by using three nested loops, which results in a time complexity of O(n^3). While this approach is simple to understand and implement, it is not very efficient for large input sizes." (written by Cody AI)

As a human, I say that for me is more afordable to memorize it as follow: each operation is like song notes. The first one is like "do", the second is "re" and so on. Then, each operation sequence of the third loop (the cubic) of the algorithm works like "do", "do, re", "do, re, mi", "do, re, mi, fa" etc. Besides the sound ordenation, what is relevant is that it need to be something that is mechanical, something that has sound and movement as well. 

In technical terms, it permits more control over each subarray element. The first calculation is over the first array element itself (0 + [0]). The second is over the first and second ([0] + [1]). The third adds one subsequent element and so until it reaches the last element and the sum will be the sum result from all array elements. This last operation can't be considered a subarray as Cody AI defines, because it is over all the array elements. For me, this cause some confusion. Only makes sense if we consider the whole group of elements of an array a subgroup of the array itself, what is weird for me. Maybe in mathematical terms this assertion is correct (all elements are part of the whole group, then the subgroup of all parts is a group) and the problem resides on my mathematics knowledge limitiations. However, the definition from the webpage mentioned first in this document is appropriate: "Maximum section sum".

### bentley2.pl quadratic

A preface: it's interesting that Cody AI just wrote "divide and conquer" when I wrote "bentley2.pl" as subtitle. "No, the second algorithm is not a "divide and conquer" approach, it's a 'greedy' approach" (Cody AI autocomplete). The cubic (bentley1) is relatively more "divided" that the quadratic (bentley2) in the sense of this sentence is commonly applied. The AI do what we want, and if we are wrong AI will complete our idea in some way it seems to make sense.

The bentley2 has different sounds for me: is like "do, re, mi, fa, sol" etc. in the first iteration on the second loop. At the second iteration it would be "re, mi, fa, sol" etc. and "mi, fa, sol" following the natural ordenation of basic notes. As this loop begins with the element of the outer loop, the elements of the array to be added to the sum are going to be cutting of from the begining as the opposite of the bentley1.  


### bentley4.pl linear  

The best algorithm which is a linear time complexity of O(n). The sum for each array sequence is added to a temporary max value (endinghere) comparing to a 0.0 value (I didn't understand why the float number). After, that sum wil be compared to a new max value that will store the biggest number from sequence.

This is like "do, re, mi, fa, sol, la, si" x n sequence, for me as it is easy to memorize relativelly to the others, of course.