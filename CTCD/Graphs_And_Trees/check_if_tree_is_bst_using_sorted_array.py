"""
Explanation:
-----------
Inorder Traversal plus using an array to hold tree elements in sorted order

Complexity:
----------
Time: O(log N)
Space: O(N)
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
        self.__arr = []

    def copy_tree_to_array(self, root):
        if root is None:
            return
        self.copy_tree_to_array(root.left)
        self.__arr.append(root.value)
        self.copy_tree_to_array(root.right)

    def check_if_bst(self, root):
        self.copy_tree_to_array(root)
        for i in range(1, len(self.__arr)):
            if self.__arr[i] <= self.__arr[i - 1]:
                return False

        return True


def main():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    is_bst = IsBst()
    print(is_bst.check_if_bst(root))

main()
