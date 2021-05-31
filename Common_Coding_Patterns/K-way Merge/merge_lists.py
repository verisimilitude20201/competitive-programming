"""
Problem:
-------
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list

Example:
-------

L1:   1 -> 3 -> 4
L2:   2 -> 6 -> 8
L3:   3 -> 6 -> 7


Result: 1 -> 2 -> 3 -> 3 -> 4 -> 6 -> 6 -> 7 -> 8

Approach:
--------
1) min_heap = []
   # Push all roots
   min_heap = [1 -> 3, 2 -> 6, 3 -> 6]
   Result = []

2) smallest = [1 -> 3]
   min_heap = [2 -> 6, 3 -> 6]
   result = [1]
   min_heap = [2 -> 6, 3 -> 4, 3 -> 6 ]

3)  smallest = [2 -> 6]
    min_heap = [3 -> 4, 3 -> 6 ]
    result = [1, 2]
    min_heap = [3 -> 4, 3 -> 6, 6 -> 8]

4)  smallest = [3 -> 4]
    min_heap = [3 -> 6, 6 -> 8]
    result = [1, 2, 3]
    min_heap = [3 -> 6, 6 -> 8, 6 -> 7]

5) smallest = [3 -> 6]
   min_heap = [6 -> 8, 6 -> 7]
   result = [1, 2, 3, 3]
   min_heap = [6 -> 8, 6 -> 7, 7 -> None]

6) smallest = [6 -> 8]
   min_heap = [6 -> 7, 7 -> None]
   result = [1, 2, 3, 3, 6]
   min_heap = [6 -> 7, 7 -> None, 8 -> None]

7) smallest = [6 -> 7]
   min_heap = [7 -> None, 8 -> None]
   result = [1, 2, 3, 3, 6]
   min_heap = [7 -> None, 8 -> None]

8) smallest = [7 -> None]
   min_heap = [8 -> None]
   result = [1, 2, 3, 3, 6, 7]
   min_heap = [8 -> None]

9) smallest = [8 -> None]
   result = [1, 2, 3, 3, 6, 7, 8]
   min_heap = []


Complexity:
---------
Time: O(N log K)
Space: O(K)

"""
from __future__ import print_function
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    result_head = None
    min_heap = []

    for list in lists:
        root = list
        if root is not None:
            heappush(min_heap, root)

    current_node = None
    while min_heap:
        node = heappop(min_heap)
        if result_head is None:
            result_head = current_node = node
        else:
            current_node.next = node
            current_node = current_node.next

        if node.next is not None:
            heappush(min_heap, node.next)

    return result_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result is not None:
        print(str(result.value) + " ", end='')
        result = result.next


main()
