"""
Complexity:
----------
Solution 1:
----------
Time: O(N log N) + O(K log K)
Space: O(N)

Solution 2:
----------
Time: O(K + log N) 
Space: O(1)
"""


class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key=lambda num: abs(x - num))

        result = []
        for i in range(k):
            result.append(sorted_arr[i])

        return sorted(result)


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        left = bisect_left(arr, x) - 1
        right = left + 1
        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        return arr[left + 1: right]