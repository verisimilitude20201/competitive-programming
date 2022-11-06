"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def __init__(self):
        self._max_diff = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def helper(root: Optional[TreeNode], max_val, min_val):
            if not root:
                return 
            
            max_val = max(root.val, max_val)
            min_val = min(root.val, min_val)
            self._max_diff = max(abs(max_val - min_val), self._max_diff)
            if root.left:
                helper(root.left, max_val, min_val)
            if root.right:
                helper(root.right, max_val, min_val)
        
        
        helper(root, -math.inf, math.inf)
        
        return self._max_diff