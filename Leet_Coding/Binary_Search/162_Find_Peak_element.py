"""
Explanation:
------------

Case 1 Descending order - 0th element peak element

-inf 4 3 2 1 -inf
     P

Case 2 Ascending order - Last element peak element

-inf 1 2 3 4 -inf
           P   

Case 3 Peak element occurs in middle

-inf 1 2 3 1 -1
         P

Complexity:
----------
Solution 1
----------
Time: O(N)
Space: O(1)

Solution 2:
----------
Time: O(log(N))
Space: O(log(N))

"""
class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        
        return len(nums) - 1

class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.find_peak_element_recursive(nums, 0, len(nums) - 1)
    
    def find_peak_element_recursive(self, nums: List[int], low: int, high: int) -> int:
        if low == high:
            return low
        
        mid = low + ((high - low) // 2)
        if nums[mid] > nums[mid + 1]:
            return self.find_peak_element_recursive(nums, low, mid)
        return self.find_peak_element_recursive(nums, mid + 1, high)