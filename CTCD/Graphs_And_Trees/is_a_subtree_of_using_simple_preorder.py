"""
Time: O(N + M)
Space: O(N + M)
"""
"""
Time: O(N + M)
Space: O(N + M)
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def contains_tree(T1, T2):
    arr1, arr2 = [], []
    get_pre_order_array(T1, arr1)
    get_pre_order_array(T2, arr2)

    string1 = "".join(arr1)
    string2 = "".join(arr2)
    print(string1)
    print(string2)
    try:
        string1.index(string2) != -1
    except:
        return False
    return True


def get_pre_order_array(T, arr):
    if T is None:
        arr.append('X')
        return

    arr.append(str(T.value))
    get_pre_order_array(T.left, arr)
    get_pre_order_array(T.right, arr)


def main():
    root1 = TreeNode(3)
    root1.left = TreeNode(4)

    root2 = TreeNode(4)
    root2.left = TreeNode(3)
    print(contains_tree(root1, root2))


main()
