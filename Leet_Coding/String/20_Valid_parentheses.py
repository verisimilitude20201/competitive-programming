"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        lefts = "[{("
        rights = "]})"
        stack = []
        for bracket in s:
            if bracket in lefts:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                previous_left = stack.pop()
                if lefts.index(previous_left) != rights.index(bracket):
                    return False
        
        return len(stack) == 0