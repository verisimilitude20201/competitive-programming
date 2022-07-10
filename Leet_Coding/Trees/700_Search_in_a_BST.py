"""
Complexity:
----------
Time: O(N) --> In worst case, we have to visit every node.
Space: O(H) Where H is the height of the tree.
"""
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)