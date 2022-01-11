"""
Explanation:
------------
1. Maintain low and high at each level of the tree

                                1  (-inf, +inf)
                   (-inf, 1) 2    3 (1, +inf)
                
2. Iterative version of 1
3. In-order, just keep track of previous value

Complexity:
----------
isValidBST1
-----------
Time: O(N)
Space: O(log N)/O(N)

isValidBST2/isValidBST3
-----------
Time: O(N)
Space: O(N)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):   
          self.val = val
          self.left = left
          self.right = right

class Solution:
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        def validate(root, low=-math.inf, high=math.inf) -> bool:
            if root is None:
                return True
            if root.val <= low or root.val >= high:
                return False
            return validate(root.left, low, root.val) and validate(root.right, root.val, high)
        
        return validate(root)
    
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [(root, -math.inf, math.inf)]
        while len(stack):
            node, low, high = stack.pop()
            if node:
                if node.val <= low or node.val >= high:
                    return False
                stack.append((node.right, node.val, high))   
                stack.append((node.left, low, node.val))                 
           
        return True
    
    def isValidBST3(self, root: TreeNode) -> bool:
        self.prev = -math.inf
        def validate(root: TreeNode) -> bool:
            if root is None:
                return True
            if not validate(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return validate(root.right)
        return validate(root)