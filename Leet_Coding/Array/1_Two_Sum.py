"""
Complexity:
----------
twoSum1 - 2-Pass HashMap
-----------------------
Time:  O(N)
Space: O(N)

twoSum2 - 1-Pass HashMap
-----------------------
Time:  O(N)
Space: O(N)

"""
class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        size = len(nums)
        for i in range(size):
            num_index[nums[i]] = i
        totals = [-1, -1]
        for j in range(size):
            second_num = target - nums[j]
            if second_num in num_index:
                second_index = num_index[second_num]
                if j != second_index:
                    totals = [j, second_index]
                    break
        
        return totals

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        size = len(nums)
        totals = [-1, -1]
        for j in range(size):
            second_num = target - nums[j]
            if second_num in num_index:
                second_index = num_index[second_num]
                totals = [j, second_index]
                break
            num_index[nums[j]] = j
        
        return totals

