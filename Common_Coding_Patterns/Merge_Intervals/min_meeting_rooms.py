"""
Problem
-------
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example:
-------
Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
occur in any of the two rooms later.

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

Approach
--------

0) [2, 3], [2, 4], [3, 5], [4, 5], minRooms = 0, min_heap = []

1) [2, 3], [2, 4], [3, 5], [4, 5], i = 0, min_heap = [[2, 3]], minRooms = max(0, len(min_heap)) = 1

2) [2, 3], [2, 4], [3, 5], [4, 5], i = 1, min_heap = [[2, 3], [2, 4]], minRooms = max(0, len(min_heap)) = 2
            
          Meeting (2, 3) has'nt ended so we need two rooms for (2, 3) and (2, 4)

3) [2, 3], [2, 4], [3, 5], [4, 5], i = 2, min_heap = [[2, 3], [2, 4]], minRooms = max(0, len(min_heap)) = 2
 
        Now meeting (2, 3) has ended so we can use the same meeting room for (3, 5)

         Remove (2, 3) ==>  min_heap = [[2, 4]]
         Add (3, 5)    ===> min_heap = [[2, 4], [3, 5]]

          minRooms = max(0, len(min_heap)) = 2

4) [2, 3], [2, 4], [3, 5], [4, 5], i = 3, min_heap = [[2, 4], [3, 5]], minRooms = max(0, len(min_heap)) = 2

            Now meeting (2, 4) has ended so we can use the same meeting room for [4, 5]
            Remove (2, 4) ==> min_heap[[3, 5]]
            Add (4, 5) ==> min_heap[[3, 5], [4, 5]]

            minRooms = max(0, len(min_heap)) = 2


0) [[1,4], [2,5], [7,9]], minRooms = 0, min_heap = []


1) [[1,4], [2,5], [7,9]], i = 0, min_heap = [[1, 4]], minRooms = max(minRooms, len(min_heap)) = 1


2) [[1,4], [2,5], [7,9]], i = 1, min_heap = [[1, 4], [2, 5]], minRooms = max(minRooms, len(min_heap)) = 2

     (1, 4) has'nt ended yet so (2, 5)  will go in a different room

3) [[1,4], [2,5], [7,9]], i = 2, min_heap = [[1, 4], [2, 5]], minRooms = max(minRooms, len(min_heap)) = 2

       For (7, 9) both (1, 4) and (2, 5) have ended so remove them from heap ==> min_heap = []
       Add (7, 9) ==> min_heap = [[7, 9]]

       minRooms = max(minRooms, len(min_heap)) = 2

1. Sort all meetings by start time. 
2. For each meeting we would need to keep track of all meetings that have ended before it started. 
3. We would need a Min-Heap data-structure to hold active meetings in sorted order of their end time.
4. For each meeting, check if the data structure has any meeting that ended before it started. If yes pop it. Continue till the min-heap has all elements popped
or it has a meeting whose ending time is greater than start time of current meeting. 
5. Length of the min_heap is the minimum number of rooms.


Complexity
----------
Time: O(N log N + log N) ~ log N for the priority queue operations and N log N for sorting.
Space: O(N) for priority Queue


"""
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)
    min_rooms = 0
    active_meetings = []
    for meeting in meetings:
        while len(active_meetings) > 0 and meeting.start >= active_meetings[0].end:
            heappop(active_meetings)
        heappush(active_meetings, meeting)
        min_rooms = max(min_rooms, len(active_meetings))

    return min_rooms


def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()
