"""
Problem
-------
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example:
-------
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Approach:
--------
Merge intervals

1. Find all non-overlapping intervals that end before the new interval starts and merge them into final merge list
2. Continue through the list and merge the current interval with the new_interval. These are overlapping intervals. 
    Overlap condition B1 <= A2
    
    a. Merge case a
        A1      A2
            B1       B2
    
    b.  Merge case b        
               A1      A2
            B1       B2

    c. Merge case c
          A1A2
        B1    B2  

     d.  A1    A2
            B1B2
     new_interval[0] = min(A1, B1)
     new_interval[1] = max(A2, B2)    
3. 

Complexity:
---------
Time: O(N)
Space: O(N) 

"""

def insert(intervals, new_interval):
    merged = []
    if len(intervals) == 0:
        return merged
    i = 0
    start = 0
    end = 1
    # Disjoint case - add all intervals that end before new_interval starts
    while i < len(intervals) and new_interval[start] > intervals[i][end]:
        merged.append([new_interval[start], new_interval[end]])
        i += 1
        # Overlapping case - Merge intervals
    while i < len(intervals) and new_interval[start] <= intervals[i][end]:
        new_interval[start] = min(new_interval[start], intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1

    merged.append([new_interval[start], new_interval[end]])

    while i < len(intervals):
        merged.append([intervals[i][start], intervals[i][start]])
    return merged


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()


