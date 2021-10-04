class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def contains_tree(T1, T2):
    if T2 is None:
        return True
    return sub_tree(T1, T2)


def sub_tree(r1, r2):
    if r1 is None:
        return False
    elif r1.value == r2.value and match_tree(r1, r2):
        return True

    return sub_tree(r1.left, r2) or sub_tree(r1.right, r2)


def match_tree(r1, r2):
    if r1 is None and r2 is None:
        return True  # Nothing left in the sub-tree
    elif r1 is None or r2 is None:
        return False  # Either of the tree is empty hence they do not match
    elif r1.value != r2.value:
        return False
    else:
        return match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right)


def main():
    root1 = TreeNode(3)
    root1.left = TreeNode(4)

    root2 = TreeNode(4)
    root2.left = TreeNode(3)
    print(contains_tree(root1, root2))


main()
