class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            l_depth = self.maxDepth(root.left)
            r_depth = self.maxDepth(root.right)
            return 1 + max(l_depth, r_depth)