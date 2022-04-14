"""
Complexity:
----------
Time: O(N)
Space: O(d) where d is the number of distinct elements in the array.
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = {}
        for i, num in enumerate(nums):
            if num not in num_index:
                num_index[num] = i
            else:
                last_index = num_index[num]
                if abs(i - last_index) <= k:
                    return True
                num_index[num] = i

        return False