"""
Problem
-------
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

             
Example:
-------
            12

		7          1            ,   Depth = 3
				              
	 9          10      5
	 
	          11

Approach
--------
BFS with a Queue. Increment depth. Return the depth when the first leaf node is detected

Complexity
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


def minimum_depth_of_binary_tree(root):
    depth = 0
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        depth += 1
        for i in range(level_size):
            current_node = queue.popleft()
            if current_node.left is None and current_node.right is None:
                return depth
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    return depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(minimum_depth_of_binary_tree(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(minimum_depth_of_binary_tree(root)))


main()
