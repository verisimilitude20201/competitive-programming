"""
Complexity:
----------
Time: O(log N)
Space: O(1)

"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        print("Value of node: " + str(self.value))


def in_order_successor(node):
    if node is None:
        return None
    if node.right is not None:
        return left_most_child(node.right)
    else:
        q = node
        x = node.parent
        while x is not None and x.left != q:
            q = x
            x = x.parent
        return x


def left_most_child(n):
    if n is None:
        return None
    while n.left:
        n = n.left

    return n


def main():
    node_20 = TreeNode(20)
    node_8 = TreeNode(8)
    node_4 = TreeNode(4)
    node_12 = TreeNode(12)
    node_10 = TreeNode(10)
    node_14 = TreeNode(14)
    node_22 = TreeNode(22)

    root = node_20
    node_8.parent = node_20
    root.left = node_8
    root.right = node_22
    node_22.parent = node_22
    root.left.left = node_4
    node_4.parent = node_8
    root.left.right = node_12
    node_12.parent = node_8
    root.left.right.left = node_10
    node_10.parent = node_12
    root.left.right.right = node_14
    node_14.parent = node_12

    successor = in_order_successor(node_14)
    print(successor.value)



main()
