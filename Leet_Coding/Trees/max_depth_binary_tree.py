"""
Complexity:
----------
maxDepthRecursive:
-----------------
Time: O(N)
Space: O(N)/O(log N) if tree is completely balanced.

"""
from typing import Optional


class Solution:
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.maxDepthRecursive(root)

    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepthRecursive(root.left) + 1
        right_depth = self.maxDepthRecursive(root.right) + 1
        return max(left_depth, right_depth)