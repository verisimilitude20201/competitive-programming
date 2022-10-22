"""
Complexity:
----------
Time: O(N log N)
Space: O(N)
"""
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for num in nums:
            digit_sum = self.get_digit_sum(num)
            dic[digit_sum].append(num)
        
        maximum_sum = -1
        for d_sum in dic:
            d_sorted_n = dic[d_sum]
            if len(d_sorted_n) > 1:
                d_sorted_n.sort(reverse=True)
                maximum_sum = max(maximum_sum, d_sorted_n[0] + d_sorted_n[1])
        
        return maximum_sum
    
    def get_digit_sum(self, num: int) -> int:
        digit_sum  = 0
        while num:
            digit_sum += (num % 10)
            num //= 10
        return digit_sum

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        maximum_sum = -1
        for num in nums:
            digit_sum = self.get_digit_sum(num)
            if digit_sum in dic:
                maximum_sum = max(maximum_sum, num + dic[digit_sum])
            
            dic[digit_sum] = max(dic[digit_sum], num)
        
        return maximum_sum
    
    def get_digit_sum(self, num: int) -> int:
        digit_sum = 0
        while num:
            digit_sum += (num % 10)
            num //= 10
        
        return digit_sum