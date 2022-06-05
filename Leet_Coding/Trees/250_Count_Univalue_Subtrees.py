"""
Complexity:
----------
Time: O(N)
Space: O(Height of the tree)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def __init__(self):
        self._count = 0
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.isUni(root)
        return self._count
    
    def isUni(self, root: Optional[TreeNode]):
        if not root:
            return
        if root.left is None and root.right is None:
            self._count += 1
            return True
        isUni = True
        if root.left:
            isUni = self.isUni(root.left) and isUni and root.val == root.left.val
        
        if root.right:
            isUni = self.isUni(root.right) and isUni and root.val == root.right.val
        
        if isUni:
            self._count += 1
        
        return isUni
            
        