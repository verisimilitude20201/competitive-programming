"""
Problem:
-------
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example:
-------
Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Approach:
--------

Following 4 cases

a.     A1   A2
         B1   B2    ===> A1 >= B1 and B1 <= A2


b.     A1      A2
         B1 B2    ===> A1 >= B1 and B1 <= A2


c.      A1  A2      
                  =====> B1 >= A1 and A1 <= B2
     B1   B2

d.   A1A2      =====> B1 >= A1 and A1 <= B2          
    B1   B2 


0) intervals_a = [[1, 3], [5, 6], [7, 9]], intervals_b = [[2, 3], [5, 7]], i = 0, j = 0, merged = []

1) Compare (1, 3) with (2, 3) ==> A overlaps with B, i = 0, j = 0, merged = [[2, 3]]

2) Compare (1, 3) with (5, 7) ==> A does not overlap with B, i = 0, j = 1, merged = [[2, 3]]

3) Compare (5, 6) with (5, 7) ==> A overlaps with B, i = 1, j = 1, merged = [[2, 3], [5, 6]]

5) Compare (7, 9) with (5, 7) ==> B overlaps with A, i = 1, j = 1, merged = [[2, 3], [5, 6], [7, 7]]


Complexity:
----------
Time: O(M + N)
Space: O(1)
"""

def merge(intervals_a, intervals_b):
    result = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
        a_overlaps_b = intervals_a[i][start] >= intervals_b[j][start] and \
                       intervals_a[i][start] <= intervals_b[j][end]

        # check if intervals overlap and intervals_a[j]'s start time lies within the other intervals_b[i]
        b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and \
                       intervals_b[j][start] <= intervals_a[i][end]

        # store the the intersection part
        if (a_overlaps_b or b_overlaps_a):
            result.append([max(intervals_a[i][start], intervals_b[j][start]), min(
                intervals_a[i][end], intervals_b[j][end])])

        # move next from the interval which is finishing first
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return result


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    # print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
