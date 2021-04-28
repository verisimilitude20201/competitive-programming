"""
Problem:
-------
Given a binary tree, populate an array to represent the averages of all of its levels.

Example:
-------
        12
    7       1
9     2  10   5

Output: [12.0, 4.0, 6.5]


Approach
--------
BFS with a queue and compute the averages of node values at each levels.

Complexity:
----------
Time: O(N)
Space: O(L) where L are the number of levels in the tree.

"""


from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_averages_binary_tree(root):
    queue = deque()
    queue.append(root)
    level_average = []
    while queue:
        level_size = len(queue)
        level_sum = 0
        for i in range(level_size):
            current_node = queue.popleft()
            level_sum += current_node.value
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        level_average.append(round(level_sum / level_size, 1))

    return level_average


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level average: " + str(level_averages_binary_tree(root)))


main()
