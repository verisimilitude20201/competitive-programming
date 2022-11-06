"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self._calc_min_depth_recursive(root)
        
    
    def _calc_min_depth_recursive(self, root: Optional[TreeNode]):
        if not root:
            return 0
        left_depth = self._calc_min_depth_recursive(root.left)
        right_depth = self._calc_min_depth_recursive(root.right)
        if left_depth == 0 or right_depth == 0:
            return max(left_depth, right_depth) + 1
        
        return min(left_depth, right_depth) + 1