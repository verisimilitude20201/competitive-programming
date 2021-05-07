"""
Problem
------
Design a class to calculate the median of a number stream. The class should have the following two methods:

    1. insertNum(int num): stores the number in the class
    2. findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example:
-------
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5

Approach
-------
Two heaps pattern

1, 4, 2, 3, 5, 6, 7, 10


1) Add 1

max_heap 			min_heap
1


2) Add 4

max_heap            min_heap 
1                     4


Median = 2.5


3) Add 2

max_heap             min_heap
1                     2
                      4


max_heap             min_heap
2                     4  
1

Median = 2


4) Add 3

max_heap             min_heap
2                     3  
1                     4

Median = 2.5 

5) Add 5


max_heap             min_heap
2                     3  
1                     4
                      5 

max_heap             min_heap
3                     4
2                     5  
1                     

Median = 3
                       

Complexity:
----------
Time: O(log N) to insert number in a min/max heap
Space: O(1) to fetch the minimum or maximum element from the heap

Note:
-----
1. We insert negative numbers in the max_heap to get the highest number at the top of the heap. Python by default supports only min_heap.

"""


from heapq import *


class MedianOfAStream:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert_num(self, num):
        if len(self.max_heap) and num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0] / 1.0


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
