"""
Complexity:
----------
Time: O(N)
Space: O(Height)

"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = None
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build_helper_tree(left_index, right_index) -> Optional[TreeNode]:
            if left_index > right_index:
                return None
            value = postorder.pop()
            index = idx_map[value]
            root = TreeNode(value)
            root.right = build_helper_tree(index + 1, right_index)
            root.left = build_helper_tree(left_index, index - 1)
            return root
        
        return build_helper_tree(0, len(inorder) - 1)
           
        
      
    