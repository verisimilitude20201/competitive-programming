"""
Explanation:
-----------
Both solutions are

Time: O(N)
Space: O(depth)
"""

class Solution1:
    def __init__(self):
        self.lca = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        current_node = root
        self.lowestCommonAncestorRecursive(current_node, p, q)
        return self.lca
    
    def lowestCommonAncestorRecursive(self, current_node: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if not current_node:
            return False
        left = self.lowestCommonAncestorRecursive(current_node.left, p, q)
        right = self.lowestCommonAncestorRecursive(current_node.right, p, q)
        mid = current_node == p or current_node == q
        if mid + left + right >= 2:
            self.lca = current_node
        return mid or left or right

class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parents = {root: None}
        ancestors = set()
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        
        while p:
            ancestors.add(p)
            p = parents[p]
        
        while q not in ancestors:
            q = parents[q]
        
        return q
        

        