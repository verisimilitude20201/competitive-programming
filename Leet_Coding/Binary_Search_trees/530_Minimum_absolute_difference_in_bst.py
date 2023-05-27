"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        in_order = self.dfs(root)
        min_difference = math.inf
        for i in range(1, len(in_order)):
            min_difference = min(min_difference, in_order[i] - in_order[i - 1])
        
        return min_difference
    
    def dfs(self, root) -> List[int]:
        if not root:
            return []
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        return left + [root.val] + right