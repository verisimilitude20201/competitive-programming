"""
Problem
-------
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

Example:
-------
            1 
        2      3
     4    5  6    7
     Output: [[1], [3, 2], [4, 5, 6, 7]]

Approach:
--------
BFS with a Queue. For odd levels, just append values. For even levels append in reverse order. We can even toggle a flag to true/false in the loop instead of counting
tree levels. 

Complexity:
----------
Time: O(N)
Space: O(N)

"""


from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def zig_zag_level_wise_traversal_binary_tree(root):
    result = []
    queue = deque()
    queue.append(root)
    tree_level = 1
    while queue:
        current_node_values = deque()
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.popleft()
            if tree_level % 2 == 0:
                current_node_values.appendleft(current_node.value)
            else:
                current_node_values.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        result.append(list(current_node_values))
        tree_level += 1

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zig Zag level order traversal: " + str(zig_zag_level_wise_traversal_binary_tree(root)))


main()
