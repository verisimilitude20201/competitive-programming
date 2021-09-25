class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        print("Value of node: " + str(self.value))


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def get_height(root):
    if root is None:
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1


def is_balanced(root):
    if root is None:
        return True
    height_diff = abs(get_height(root.left) - get_height(root.right))
    if height_diff > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    is_balanced(root)


main()
