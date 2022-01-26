"""
Complexity:
----------
duplicateZeros1
---------------
    Time: O(N^2)
    Space: O(1)
"""
class Solution:
    def duplicateZeros1(self, arr: List[int]) -> None:
        k = len(arr) - 1
        for i in range(len(arr) - 1, -1, 0):
            if arr[i - 1] == 0:
                while k > i:
                    arr[k] = arr[k - 1]
                    k -= 1
                arr[i] = 0
            k = len(arr) - 1