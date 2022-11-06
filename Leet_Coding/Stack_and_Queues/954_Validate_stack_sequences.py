"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return j == len(popped)