"""
Complexity:
----------
Time: O(log7(N))
Space: O(log7N) Where N is the number
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        n = abs(num)
        num_arr = []
        while n:
             num_arr.append(str(n % 7))
             n //= 7
        
        num_str = "".join(num_arr)
        
        
        return  ("-" + num_str[::-1] if num < 0 else num_str[::-1]) or "0"