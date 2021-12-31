"""
Complexity:
----------
Time: O(N)
Space: O(height)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        temp = None
        stack = []
        post_order = []
        if root is None:
            return []
        while current or len(stack):
            if current:
                stack.append(current)
                current = current.left
            else:
                temp = stack[-1].right
                if temp is None:
                    temp = stack.pop()
                    post_order.append(temp.val)
                    while len(stack) and stack[-1].right == temp:
                        temp = stack.pop()
                        post_order.append(temp.val)
                else:
                    current = temp

        return post_order