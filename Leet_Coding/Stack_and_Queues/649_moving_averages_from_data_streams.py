"""
Explanation:
-----------
Use a queue of size 3. 

Complexity:
----------
Time: O(1)
Space: O(1)
"""

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self._size = size
        self._queue = deque([None] * self._size)

    def next(self, val: int) -> float:
        if len(self._queue) == self._size:
            self._queue.popleft()
        self._queue.append(val)
        total = 0
        count_of_elements = 0
        for i in range(len(self._queue)):
            if self._queue[i] is not None:
                total += self._queue[i]
                count_of_elements += 1
        return total / count_of_elements