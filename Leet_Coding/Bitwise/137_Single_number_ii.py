"""
Complexity:
----------
Solution 1
-----------
Time: O(N log N)
Space: O(1)


Solution 2
-----------
Time: O(N)
Space: O(N)

"""
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return nums[0]

        for i in range(0, len(nums) - 1, 3):
            if nums[i] == nums[i + 1]:
                continue
            else:
                return nums[i]
        
        return nums[-1]

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        return ((3 * sum(num_set)) - sum(nums)) // 2

class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        loner  = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                ith_bit = (num >> i) & 1
                bit_sum += ith_bit

            loner_bit = bit_sum % 3
            loner = loner | ( loner_bit << i)

        if loner >= (1 << 31):
            loner = loner - (1 << 32)

        return loner