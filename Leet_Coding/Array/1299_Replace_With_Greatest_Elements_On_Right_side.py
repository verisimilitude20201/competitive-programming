"""
Explanation:
-----------
Iterate from last element
1. Store a copy of the element in max_right initialized to -1
2. Update the current element of array to max_right
3. Update max_right to max of tmp and current max_right

Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = max_right
            max_right = max(tmp, max_right)

        return arr