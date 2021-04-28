"""
Problem:
-------
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. 
You should populate the values of all nodes in each level from left to right in separate sub-arrays.

Example:
-----------

                    1
                2        3
            4      5  6      7

        Output: [[4, 5, 6, 7], [2, 3], [1]]  

Approach:
--------
Two approaches

1. reverse_level_order_traversal_binary_tree1: Uses BFS using an auxillary queue. Also using an additional stack to hold the value sub-arrays of all levels and a final result list
that gets populated on traversing the stack. So we use 3 extra variables here. Can this be minimized to just 2?

2. reverse_level_order_traversal_binary_tree2: Same as reverse_level_order_traversal_binary_tree1 except we treat the result as a doubly ended-queue and append values from the front of the queue


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


def reverse_level_order_traversal_binary_tree1(root):
    queue = deque()
    queue.append(root)
    stack = deque()
    result = []
    while queue:
        current_node_values = []
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.popleft()
            current_node_values.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        stack.append(current_node_values)

    while stack:
        current_node_values = stack.pop()
        result.append(current_node_values)

    return result


def reverse_level_order_traversal_binary_tree2(root):
    queue = deque()
    queue.append(root)
    result = deque()
    while queue:
        current_node_values = []
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.popleft()
            current_node_values.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        result.appendleft(current_node_values)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(reverse_level_order_traversal_binary_tree1(root)))
    print("Reverse level order traversal: " + str(reverse_level_order_traversal_binary_tree2(root)))



main()
