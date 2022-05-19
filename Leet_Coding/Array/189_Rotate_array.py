"""
Complexity:
----------
Solution 1
----------
Time: O(N * K)
Space: O(1)

Solution 2
----------
Time: O(N)
Space: O(N)
"""
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        for _ in range(k):
            previous = nums[-1]
            for i in range(len(nums)):
                nums[i], previous = previous, nums[i]


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
     
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        
        nums[:] = a

solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums, 3)
print(nums)

