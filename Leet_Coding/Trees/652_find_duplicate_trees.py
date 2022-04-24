"""
Complexity:
----------
Time: O(N^2): Because we use a tuple and a Python tuple does'nt cache it's hashes. It recomputes
them every time for every item. Use a frozen set to get a linear time complexity.
Space: O(N)
"""
class Solution:
    def __init__(self) -> None:
        self.subtree_map = defaultdict(list)

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse_tree(root)
        return [roots[0] for roots in self.subtree_map.values() if roots[1:]]

    def traverse_tree(self, root: Optional[TreeNode]) -> str:
        if root:
            left_value = self.traverse_tree(root.left)
            right_value = self.traverse_tree(root.right)
            key = root.val, left_value, right_value
            self.subtree_map[key].append(root)

            return key