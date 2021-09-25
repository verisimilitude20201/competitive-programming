"""
Explanation:
-----------
A modification of in-oder
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        print("Value of node: " + str(self.value))


def create_linked_lists_of_binary_tree(root):
    lists = []
    create_linked_lists_of_binary_tree_recursive(root, lists, 0)
    return lists


def create_linked_lists_of_binary_tree_recursive(root, lists, level):
    if root is None:
        return;
    l = None
    if len(lists) == level:
        l = []
        lists.append(l)
    else:
        l = lists[level]
    l.append(root.value)
    create_linked_lists_of_binary_tree_recursive(root.left, lists, level + 1)
    create_linked_lists_of_binary_tree_recursive(root.right, lists, level + 1)




def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    lists = create_linked_lists_of_binary_tree(root)
    print(lists)



main()