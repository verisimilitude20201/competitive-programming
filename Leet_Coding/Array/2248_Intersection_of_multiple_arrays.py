class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            for x in num:
                count[x] += 1
        
        n = len(nums)
        common_elements = []
        for num in count:
            if count[num] == n:
                common_elements.append(num)
        common_elements.sort()
        
        return common_elements