"""
Problem:
-------
Given an array of points in a 2D2D2D plane, find ‘K’ closest points to the origin.

Example:
-------
Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

Approach:
--------
Euclidean distance of a point(x, y) from origin (0, 0) is sqrt(x^2 + y^2). Use a min-heap

Complexity:
----------
Space: O(K)
Time: O(N * Log K)
"""

from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = (self.x * self.x) + (self.y * self.y)

    def __lt__(self, other):
        return self.distance < other.distance

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


from heapq import *


def find_closest_points(points, k):
    min_heap = []
    for i in range(k):
        point = points[i]
        heappush(min_heap, point)

    for i in range(k, len(points)):
        if points[i] < min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, points[i])

    return list(min_heap)


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
