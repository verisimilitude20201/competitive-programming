"""
Explanation:
-----------
The challenge here is to compute the right bound. Since array is sorted in increasing order, keep
on doubling the right's value till the element at the right index is greater than target. Then, binary 
search

Complexity:
----------
Time: O(log N)
Space: O(1)
"""
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
        left = 0,
        right = 1
        while reader.get(right) < target:
            right <<= 1

        while left <= right:
            pivot = left + ((right - left) // 2)
            num = reader.get(pivot)
            if num == target:
                return pivot
            elif num < target:
                left = pivot + 1
            else:
                right = pivot - 1

        return -1