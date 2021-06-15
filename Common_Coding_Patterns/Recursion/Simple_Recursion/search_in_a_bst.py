class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None

        return self.search_bst_recursive(root, val)

    def search_bst_recursive(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return root

        if root.val == val:
            return root
        else:
            if root.val > val:
                return self.search_bst_recursive(root.right, val)

            if root.val < val:
                return self.search_bst_recursive(root.left, val)


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)

solution = Solution()

print(solution.searchBST(root, 2))
