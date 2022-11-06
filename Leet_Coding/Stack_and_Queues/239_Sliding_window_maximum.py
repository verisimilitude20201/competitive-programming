"""
Complexity:
----------
Time: O(N)
Space: O(1) // Because only 3 elements reside in the queue
"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q = deque([])
        answers = []
        for i in range(len(nums)):
            while Q and nums[Q[-1]] < nums[i]:
                Q.pop()
                
            Q.append(i)
            if Q[0] + k == i:
                Q.popleft()
            
            if i >= k - 1:
                answers.append(nums[Q[0]])
        
        return answers