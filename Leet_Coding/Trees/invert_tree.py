"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.appendleft(root)
        while len(q):
            node = q.pop()
            if node is None:
                break
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
         
        return root