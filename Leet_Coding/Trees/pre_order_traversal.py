"""
Explanation:
------------
preorderTraversal1 we recurse through all nodes and we also require a Space complexity of O(N) to hold the 
Stack frames

preorderTraversal2 Since we are iteratively using a stack, we must first push the right node and then the left
node.

Complexity:
---------
    preorderTraversal1
    -----------------
    Time: O(N)
    Space: O(N)

    preorderTraversal2
    ------------------
    Time: O(N)
    Space: O(N)
"""
class Solution:
    def __init__(self):
        self.pre_order = []
    
    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.pre_order

    def dfs(self, root: Optional[TreeNode]):
        if root:
            self.pre_order.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
    
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        return self.bfs(root)

    def bfs(self, root: Optional[TreeNode]):
        stack = []
        if root is None:
            return self.pre_order
        
        stack.append(root)
        while stack:
            node = stack.pop()
            self.pre_order.append(node.val)
            if node.right:
                stack.append(node.right)
        
            if node.left:
                stack.append(node.left)
            
        return self.pre_order
    
        
        