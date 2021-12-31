"""
Complexity:
-----------
inorderTraversal1:
----------------
Time: O(N)
Space: O(1)

inorderTraversal2:
-----------------
Time: O(N)
Space: O(N)

inorderTraversal3:
-----------------
Time: O(N)
Space: O(N)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        inorder = []
        while current:
            if current.left is None:
                inorder.append(current.val)
                current = current.right
            else:
                prev = current.left
                while prev.right and prev.right != current:
                    prev = prev.right
                if prev.right is None:
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None
                    inorder.append(current.val)
                    current = current.right
                    
        return inorder
    
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_traversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
            if root.left:
                self.inorder_traversal_recursive(root.left)
            self.output.append(root.val)
            if root.right:
                self.inorder_traversal_recursive(root.right)
        
        self.inorder_traversal_recursive(root)
        return self.output
    
    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        current = root
        while current or len(stack) > 0:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            output.append(current.val)
            current = current.right
        
        return output