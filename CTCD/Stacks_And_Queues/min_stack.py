"""
Explanation:
-----------
This solution maintains the current min for every element that has been added to the stack

Complexity:
----------
Time: O(1) Amortized
Space: O(N)
"""
import math


class NodeWithMin:
    def __init__(self, min_value, value):
        self.min_value = min_value
        self.value = value


class StackWithMin:
    def __init__(self):
        self._data = []

    def push(self, element):
        new_min = min(element, self._current_minimum())
        self._data.append(NodeWithMin(new_min, element))

    def _current_minimum(self):
        if len(self._data) == 0:
            return None
        node_with_min = self._data.pop()
        return node_with_min.min_value

    def _current_minimum(self):
        if len(self._data) == 0:
            return -math.inf
        else:
            return self.peek()

    def peek(self):
        top_node = self._data[-1]

        return top_node.value


def main():
    stack_with_min = StackWithMin()
    stack_with_min.push(5)
    stack_with_min.push(6)
    stack_with_min.push(3)
    stack_with_min.push(7)


main()
