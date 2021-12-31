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

    preorderTraversal3:
    ------------------
    Time: O(N)
    Space: O(1)
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
    
    def preorderTraversal_iterative(self, root):
        output = []
        if root is None:
            return []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
       
        return output
    
    def preorderTraversal3(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder = []
        current = root
        while current:
            if current.left is None:
                preorder.append(current.val)
                current = current.right
            else:
                prev = current.left
                while prev.right and prev.right != current:
                    prev = prev.right
                
                if prev.right is None:
                    preorder.append(current.val)
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None
                    current = current.right
        
        return preorder
    
        
        