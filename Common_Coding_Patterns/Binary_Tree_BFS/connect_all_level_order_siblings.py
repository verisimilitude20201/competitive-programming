"""
Problem
------
Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.

Example:
-------
                1
			
			2         3

	   4       5   6       7

               
                   1 -->
			
		-->	2      ->          3  -->

	  --> 4  ->     5  ->  6   ->    7  --> None

      In addition to the pointers at each level, we have 1 points to 2, 3 points to 4

Approach:
--------
BFS with a queue

1. Keep track of all previous nodes and connect them to the current node.
2. Do not reset prev_node to None. 

Complexity
----------
Time: O(N)
Space: O(N)

"""
from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    queue = deque()
    queue.append(root)
    prev_node = None
    current_node = None
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            if current_node is not None:
               prev_node = current_node
            current_node = queue.popleft()
            if prev_node is not None:
                prev_node.next = current_node
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()
main()