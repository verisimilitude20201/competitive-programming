"""
Explanation:
-----------
0) S1 = [], min_stack = []

1) Push 5
  S1 = [5], min_stack = [5]

2) Push 6
S1 = [5, 6],  min_stack = [5]

3) Push 3
S1 = [5, 6, 3], min_stack = [5, 3]

4) Push 7
S1 = [5, 6, 3, 7], min_stack = [5, 3]

Complexity:
----------
Time: O(1) Amortized
Space: O(N)

Note:
-----
This is more space efficient than min_stack.py. If the first stack has large number of integers in ascending order, then the 0th element would be in the second stack
and that would be minimum. So second stack will just have one element.

"""
import math


class StackWithMin2:
    def __init__(self):
        self._data = []
        self._mins = []

    def push(self, element):
        if element <= self._current_minimum():
            self._mins.append(element)
        self._data.append(element)

    def pop(self):
        value = self._data.pop()
        if value == self._current_minimum():
            self._mins.pop()

        return value

    def _current_minimum(self):
        if len(self._mins) == 0:
            return math.inf
        else:
            return self._mins[-1]


def main():
    stack_with_min2 = StackWithMin2()
    stack_with_min2.push(5)
    stack_with_min2.push(6)
    stack_with_min2.push(3)
    stack_with_min2.push(7)


main()
