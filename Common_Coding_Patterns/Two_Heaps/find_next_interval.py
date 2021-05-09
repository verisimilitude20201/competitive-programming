"""
Problem:
-------
Given an array of intervals, find the next interval of each interval. 
In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

Write a function to return an array containing indices of the next interval of each input interval. 
If there is no next interval of a given interval, return -1. It is given that none of the intervals have the same start point

Example:
--------
Input: Intervals [[2,3], [3,4], [5,6]]
Output: [1, 2, -1]
Explanation: The next interval of [2,3] is [3,4] having index ‘1’. Similarly, the next interval of [3,4] is [5,6] having index ‘2’. 
There is no next interval for [5,6] hence we have ‘-1’.

Approach:
--------

0) 

Input: Intervals [[3,4], [1,5], [4,6]]
Output: [2, -1, -1]


1) 

max_start_heap = [(4, 2), (3, 0), (1, 1)]
max_end_heap = [(6, 2), (5, 1), (4, 0)]


2) result = [-1, -1, -1]

i)  
    top_end, end_index = (6, 2)
    max_start_heap = [(4, 2), (3, 0), (1, 1)]
    max_end_heap = [(5, 1), (4, 0)]
   

    Current interval in max_start_heap's start time is not greater than top_end i.e 4 >= 6 is false


ii) top_end, end_index = (5, 1)
    max_start_heap = [(4, 2), (3, 0), (1, 1)]
    max_end_heap = [(4, 0)]

     Current interval in max_start_heap's start time is not greater than top_end i.e 4 >= 5 is false

iii) top_end, end_index = (4, 0)
     max_start_heap = [(4, 2), (3, 0), (1, 1)]
     max_end_heap = []

     a. Current interval in max_start_heap's start time is  greater than top_end i.e 4 >= 4 is true
        top_start, start_end = 4, 2
     
     b. Current interval in max_start_heap's start time is  not greater than top_end i.e 3 >= 4 is true
     max_start_heap = [(3, 0), (1, 1)]

 iv) result = [2, -1, -1] we have set the start_index = 2 at the end_index = 0 in result



Complexity:
---------
Time: O(N log N)
Space: O(N)

"""

from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    n = len(intervals)
    result = [-1] * n
    max_start_heap = []
    max_end_heap = []
    for i in range(n):
        heappush(max_start_heap, (-intervals[i].start, i))
        heappush(max_end_heap, (-intervals[i].end, i))

    for j in range(n):
        top_end, end_index = heappop(max_end_heap)
        if -max_start_heap[0][0] >= -top_end:
            while max_start_heap and -max_start_heap[0][0] >= -top_end:
                top_start, start_index = heappop(max_start_heap)
            result[end_index] = start_index
            heappush(max_start_heap, (top_start, start_index))

    return result


def main():
    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
