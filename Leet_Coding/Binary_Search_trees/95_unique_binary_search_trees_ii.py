"""
Explanation
-----------
1. Create root node by cycling through [1, 3]
2. Use the list [start, currentRootVal - 1] to form left trees
3. Use the list [currentRootVal + 1, right] to form the right trees
4. For each unique combination of left tree and right tree attach to current root
5. Add each root to a list
6. Return the list

"""
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.helper(1, n)
    
    def helper(self, start, end) -> List[Optional[TreeNode]]:
        if start > end:
            return [None]
        all_trees = []
        for i in range(start, end + 1):
            left_trees = self.helper(start, i - 1)
            right_trees = self.helper(i + 1, end)
            for lt in left_trees:
                for rt in right_trees:
                    tree_node = TreeNode(i)
                    tree_node.left = lt
                    tree_node.right = rt
                    all_trees.append(tree_node)
        
        return all_trees