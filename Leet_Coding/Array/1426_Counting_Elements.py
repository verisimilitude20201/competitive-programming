"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        arr_set = set(arr)
        for num in arr:
            if num + 1 in arr_set:
                count += 1
        
        return count