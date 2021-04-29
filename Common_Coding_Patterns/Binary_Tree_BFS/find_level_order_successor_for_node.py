"""
Problem
------
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.

Example:
-------
            12

		7          1             
				              
	 9          10      5,  
	 
	 node = 9
	 level order sucessor is 10
	 Queue = [12]

Approach:
--------
BFS with a queue. 

1. After adding the left and right children back to queue, check if the current_node equals the node whose sucessor we have to find.
2. If yes, return the successor by popping the next node off the queue.

Complexity:
---------
Time: O(N)
Space: O(N)

"""

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_level_order_successor_for_node(root, node_value):
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.popleft()
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
            if current_node.value == node_value:
                level_order_successor = queue.popleft()
                return level_order_successor

    return None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_level_order_successor_for_node(root, 12)
    if result:
        print(result.value)
    result = find_level_order_successor_for_node(root, 9)
    if result:
        print(result.value)


main()
