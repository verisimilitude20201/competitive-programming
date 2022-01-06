"""
hasPathSum1
-----------
Time: O(N)
Space: O(N) / O(log(N))

hasPathSum2
-----------
Time: O(N)
Space: O(N) / O(log(N))
"""
class Solution:
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.hasPathSumRecursive(root, targetSum)
        
    def hasPathSumRecursive(self, root: Optional[TreeNode], current_sum: int) -> bool:
        if root is None:
            return False
        current_sum -= root.val
        if root.left is None and root.right is None:
            return current_sum == 0
        
        return self.hasPathSumRecursive(root.left, current_sum) or self.hasPathSumRecursive(root.right, current_sum)

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        S = [(root, targetSum - root.val)]
        while len(S):
            node, current_sum = S.pop()
            if node.left is None and node.right is None and current_sum == 0:
                return True
            
            if node.right:
                S.append((node.right, current_sum - node.right.val))
            if node.left:
                S.append((node.left, current_sum - node.left.val))

        return False