"""
Complexity:
----------
Solution1
---------
Time: O(N)
Space: O(N)

Solution 2:
----------
Time: O(K): K is the index of the closest element. In average case, we do K times push and K times pop for an balanced tree. In Worst case for an unbalanced tree, it's O(K + H) where H is height of the tree.
Space: O(H) Where H is the height of the tree

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
    def __init__(self):
        self._in_order = []
        
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.in_order(root)
        return min(self._in_order, key=lambda x: abs(target - x))
    
    def in_order(self, root):
        if not root:
            return []
        self.in_order(root.left)
        self._in_order.append(root.val)
        self.in_order(root.right)

class Solution2:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        S = []
        current = root
        pred = -float("inf")
        while S or current:
            while current:
                S.append(current)
                current = current.left
            current = S.pop()
            if pred <= target < current.val:
                return min(pred, current.val, key=lambda x: abs(target - x))
            
            pred = current.val
            current = current.right
        
        return pred