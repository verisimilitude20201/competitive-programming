"""
Explanation:
-----------
1. Uses a Set to store the value of all nodes of BST. Does not use BST property


Complexity:
---------
findTarget1
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def findTarget1(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        vals = set()
        return self.search1(root, vals, k)
        
    def search1(self, root: TreeNode, vals, k: int) -> bool:
        if root is None:
            return False
        if (k - root.val) in vals:
            return True
        vals.add(root.val)
        return self.search(root.left, vals, k) or self.search(root.right, vals, k)