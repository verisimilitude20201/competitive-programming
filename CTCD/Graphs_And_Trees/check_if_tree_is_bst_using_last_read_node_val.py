"""
Explanation:
-----------
In-order traversal and maintain only the last traversed node's value

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
        self._prev_value = None

    def check_if_bst_using_previous_node(self, root):
        if root is None:
            return True
        if not self.check_if_bst_using_previous_node(root.left):
            return False
        if self._prev_value is not None and self._prev_value >= root.value:
            return False
        self._prev_value = root.value
        if not self.check_if_bst_using_previous_node(root.right):
            return False

        return True


def main():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    is_bst = IsBst()
    print(is_bst.check_if_bst_using_previous_node(root))


main()
