"""
Complexity:
----------
Time: O(4^N / SQRT(N))
Space: O(2N)
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parenthesis = []
        def backtrack(left_count, right_count):
            if len(parenthesis) == 2 * n:
                res.append("".join(parenthesis))
                return
            
            if left_count < n:
                parenthesis.append("(")
                backtrack(left_count + 1, right_count)
                parenthesis.pop()
            
            if right_count < left_count:
                parenthesis.append(")")
                backtrack(left_count, right_count + 1)
                parenthesis.pop()
        
        backtrack(0, 0)
        return res