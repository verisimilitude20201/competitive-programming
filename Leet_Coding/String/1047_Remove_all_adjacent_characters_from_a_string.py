"""
Complexity:
---------0
Time: O(N)
Space: O(N)
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack) and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        if len(stack) == 0:
            return ""
        
        return "".join(stack)