"""
Complexity:
----------
Time: O(N * log N)
Space: O(N)
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_minimal_bst(arr):
    return create_minimal_bst_recursive(arr, 0, len(arr) - 1)


def create_minimal_bst_recursive(arr, start, end):
    if end < start:
        return None
    mid = int((start + end) / 2)
    tree_node = TreeNode(arr[mid])
    tree_node.left = create_minimal_bst_recursive(arr, start, mid - 1)
    tree_node.right = create_minimal_bst_recursive(arr, mid + 1, end)

    return tree_node


create_minimal_bst([1, 2, 3])