"""
Problem:
-------
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example:
-------
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from 
the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Approach:
--------

Complexity:
---------
Time: O(K Log M)
Space: O(M)

"""

from heapq import *


class Element:
    def __init__(self, current_element, current_index, current_list):
        self.current_element = current_element
        self.current_index = current_index
        self.current_list = current_list

    def __lt__(self, other):
        return self.current_element < other.current_element


def find_kth_smallest_element(lists, k):
    number = -1
    min_heap = []
    merged_list = []
    for l in lists:
        element = Element(l[0], 0, l)
        heappush(min_heap, element)

    while min_heap:
        smallest_element = heappop(min_heap)
        merged_list.append(smallest_element.current_element)
        current_index = smallest_element.current_index
        current_index += 1
        if current_index < len(smallest_element.current_list):
            heappush(min_heap, Element(smallest_element.current_list[current_index], current_index,
                                       smallest_element.current_list))

    if (k - 1) < len(merged_list):
        return merged_list[k - 1]

    return -1

def main():
  print("Kth smallest number is: " +
        str(find_kth_smallest_element([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()