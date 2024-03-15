import math
import random

class Stats:

    def quicksort(self, lyst):
        if len(lyst) <= 1:
            return lyst

        pivot = lyst[len(lyst) // 2]
        smaller = [x for x in lyst if x < pivot]
        larger = [y for y in lyst if y > pivot]

        return self.quicksort(smaller) + [pivot] + self.quicksort(larger)
    
    def mergesort(self, lyst):
        if len(lyst) <= 1:
            return lyst

        middle = len(lyst) // 2
        print('middle, element: ', middle, lyst[middle])
        left = self.mergesort(lyst[:middle])
        print('left, lyst: ', left, lyst)
        right = self.mergesort(lyst[middle:])
        print('middle, right, lyst: ', middle, right, lyst)
        # return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:]
        result += right[j:]

        return result

    def median(self, lyst):
        print(lyst)
        median_list = self.sort_list(lyst)
        size = len(median_list)
        index = size / 2
        print(lyst)
        print(median_list)
        print(size, median_list[math.floor(index)])
        if index is not int(index):
            return median_list[math.floor(index)]
        else:
            return (median_list[index] + median_list[index + 1]) / 2 



s = Stats()
lyst = [360, 501, 28, 602, 474, 647, 135, 790, 184, 509]
# for x in range(1):
# for i in range(10):
#     n = random.randrange(1,1000)
#     lyst.append(n)
print('unsorted lyst: ', lyst)
print('sorted lyst: ', s.mergesort(lyst))
print('-------------------------------------------')

# lyst = [1,2,3]
# print(lyst[:2])