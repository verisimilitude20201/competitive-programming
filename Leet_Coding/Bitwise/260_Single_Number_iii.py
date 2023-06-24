class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bit_mask = 0
        for num in nums:
            bit_mask ^= num

        diff = bit_mask & (-bit_mask)
        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bit_mask ^ x]