"""
Complexity:
----------
Time: O(S + T)
Space: O(S + T)
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.back_space(s) == self.back_space(t)
    
    def back_space(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "#":
                stack.append(c)
            elif len(stack):
                stack.pop()
        
        if len(stack):
            return "".join(stack)
        
        return ""