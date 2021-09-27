"""
Explanation:
-----------
In-order traversal and compute the min and max at each node to check if its a BST.

Complexity:
---------
Time: O(N) (We touch all nodes)
Space: O(log N)
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        print("Value of node: " + str(self.value))


class IsBst:
    def __init__(self):
        pass

    def check_if_bst_using_min_max(self, root, min1=None, max1=None):
        if root is None:
            return True

        if (min1 is not None and min1 >= root.value) or (max1 is not None and max1 < root.value):
            return False

        if not self.check_if_bst_using_min_max(root.left, min1, root.value) or not self.check_if_bst_using_min_max(root.right, root.value, max1):
            return False

        return True


def main():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    is_bst = IsBst()
    print(is_bst.check_if_bst_using_min_max(root))


main()
