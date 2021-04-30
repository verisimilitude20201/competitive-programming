"""
Problem
-------
Given a binary tree, return an array containing nodes in its right view. 
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

Example:
-------
                 1
			
			2         3

	   4       5   6       7 

       Right Nodes = [1, 3, 7]

Approach:
--------
BFS with a queue. The last element in the queue for a level is the right-most node. Similarly, the left element is the first node.

Complexity:
---------
Time:  O(N)
Space: O(N)

"""

from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def get_right_nodes_of_binary_tree(root):
    queue = deque()
    queue.append(root)
    prev_node = None
    current_node = None
    right_nodes = []
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.popleft()
            if i == level_size - 1:
                right_nodes.append(current_node)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    return right_nodes


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = get_right_nodes_of_binary_tree(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
