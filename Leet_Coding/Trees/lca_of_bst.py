"""
Explanation:
------------
1. LCA is the first node for which p and q don't lie on the same sub-tree. Apply properties of BST, move 
left if the root's val is less than both p and q and move right otherwise. If both condition not satisfy
return the root which is the LCA
2. Iterative way does the same thing, no stack needed

Complexity:
----------
1. Time: O(N), Space: O(N)
2. Time: O(N), Space: O(1)

"""
class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        parent_val = root.val
        if p.val < parent_val and q.val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > parent_val and q.val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root