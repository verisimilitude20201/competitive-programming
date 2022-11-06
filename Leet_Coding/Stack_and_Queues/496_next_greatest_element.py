"""
Complexity:
----------

Solution 1
----------
Time: O(M * N)
Space: O(1) // Don't consider time complexity for output array.

Solution 2
----------
Time: O(M + N)
Space: O(M) 
"""
class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            found = False
            for num2 in nums2:
                if num == num2:
                    found = True
                if found and num2 > num:
                    ans[i] = num2
                    break

class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater_element = {}
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater_element[stack.pop()] = num
            
            stack.append(num)
        while stack:
            next_greater_element[stack.pop()] = -1
        
        ans = []
        for i, num in enumerate(nums1):
            ans.append(next_greater_element.get(num, -1))
        
        return ans