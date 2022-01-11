"""
Complexity:
----------
searchBST1
---------
Time: O(H) Where H is the height of the tree
Space: O(H) Where H is the height of the tree

searchBST2
---------
Time: O(H)
Space: O(1)

O(N) / O(log(N)) depending on whether the tree is balanced or not

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST1(self, root:TreeNode, val: int):
        if root is None or val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
    
    def searchBST2(self, root:TreeNode, val: int):
        while root:
            if val == root.val:
                break
            elif val < root.val:
                root = root.left
            else:
                root = root.right

        return root
        