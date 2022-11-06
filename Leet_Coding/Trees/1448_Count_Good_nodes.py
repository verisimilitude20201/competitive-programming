"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
import math


class Solution:
    def __init__(self):
        self._good_cnt = 0
        
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.find_good_nodes(root, -math.inf)
        
        return self._good_cnt
    
    def find_good_nodes(self, root: TreeNode, max_seen_so_far: int):
        if not root:
            return
        self._good_cnt += (root.val >= max_seen_so_far)
        self.find_good_nodes(root.left, max(max_seen_so_far, root.val))
        self.find_good_nodes(root.right, max(max_seen_so_far, root.val))