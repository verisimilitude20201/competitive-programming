"""
Complexity:
----------
Time: O(N)
Space: O(Height)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        root = None
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        def build_tree(left_index, right_index) -> Optional[TreeNode]:
            if left_index > right_index:
                return None
            nonlocal preorder_index
            value = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(value)
            index = idx_map[value]
            root.left = build_tree(left_index, index - 1)
            root.right = build_tree(index + 1, right_index)
            
            return root
        
        return build_tree(0, len(inorder) - 1)
        