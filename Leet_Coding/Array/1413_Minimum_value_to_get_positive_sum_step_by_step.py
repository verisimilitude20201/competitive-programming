"""
Complexity:
----------

Solution1:
---------
Time:
    N = length of array
    M = absolute value of the lower bound in the array.

    If the array is nums = [1, 1, 1, 1, -1, -2, -3, -4, -5], 
    minimum valid start value = (n / 2) * (m - 1) + 1

    Each iteration starts with startValue and we iterate (n/2) + 1 times.
    So time complexity O(n^2 * m)

Space: O(1)

Solution 2:
-----------
Time: O(N)
Space: O(1)

Solution 3:
-----------
Time: O(log(NM) * N)
Space: O(1)

"""
class Solution1:
    def minStartValue1(self, nums: List[int]) -> int:
        start_value = 1
        while True:
            total = start_value
            is_valid = True
            for num in nums:
                total += num
                if total < 1:
                    is_valid = False
                    break
            
            if is_valid:
                return start_value
            else:
                start_value += 1

class Solution2:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        start_value = 0
        for num in nums:
            total += num
            start_value = min(start_value, total)
        
        return -start_value + 1
    


class Solution3:
    def minStartValue(self, nums: List[int]) -> int:
        left = 1
        right = abs(min(nums)) * len(nums) + 1
        while left < right:
            middle = (left + right) // 2
            is_valid = True
            total = middle
            for num in nums:
                total += num
                if total < 1:
                    is_valid = False
                    break
            
            if is_valid:
                right = middle
            else:
                left = middle + 1
        
        return left
                