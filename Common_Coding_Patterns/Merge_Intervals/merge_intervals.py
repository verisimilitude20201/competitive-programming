"""
Problem
-------
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals

Example:
--------
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].

Approach
--------
Merge intervals.

1. Sort all intervals such that a.start <= b.start. If we do this, we just need to take care of b.end
2. Check now if A overlaps B. i.e. if B.end <= start. If so, adjust the interval by taking max of B.end and A.end and update merge interval

0) [[1,4], [2,6], [3,5]], start=None, end=None

1) Sort in ascending order of start interval

 [[1,4], [2,6], [3,5]], start=None, end=None


2) [[1,4], [2,6], [3,5]], start=1, end=4, interval.start = 2, interval.end  = 6, 6 <= 4, mergedIntervals = []

   [[1,4], [2,6], [3,5]], start=2, end=6, interval.start = 2, interval.end  = 6, 6 <= 4, mergedIntervals = [[1, 4]]

3) [[1,4], [2,6], [3,5]], start=2, end=6, interval.start = 3, interval.end  = 5, 5 <= 6, mergedIntervals = [[1, 4]]

   [[1,4], [2,6], [3,5]], start=2, end=6, interval.start = 3, interval.end  = 5, 5 <= 6, mergedIntervals = [[1, 4], [2, 6]]

Complexity:
----------
Time: O(N Log N) + O(N) ~ O(N Log N)
Space: O(N)

"""

from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    if len(intervals) < 2:
        return intervals
    merged = []
    intervals.sort(key=lambda x: x.start)
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        if intervals[i].start <= end:
            end = max(end, intervals[i].end)
        else:
            merged.append(Interval(start, end))
            start = intervals[i].start
            end = intervals[i].end
    merged.append(Interval(start, end))

    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
