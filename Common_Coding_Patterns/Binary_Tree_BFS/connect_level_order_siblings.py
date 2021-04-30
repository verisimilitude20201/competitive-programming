"""
Problem:
-------
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.

Example:
-------
                1
			
			2         3

	   4       5  6       7

              Output
-------------------------------------
                 1
			
			2   -->           3

	   4  -->    5  -->   6 -->    7  
Approach
--------
BFS using a queue. The only difference is maintain a prev_node pointer..

0)
				1
			
			2         3

	   4       5  6       7 

	   Queue = [1], current_node = None, prev_none = None



1) 

				1
			
			2         3

	   4       5  6       7 

	   Queue = [1], current_node = None, prev_none = None, level_size = 1


	   			1
			
			2         3

	   4       5  6       7 

	   Queue = [], current_node = 1 -> None, prev_none = None, level_size = 1, i = 0


	            1
			
			2         3

	   4       5  6       7 

	   Queue = [2, 3], current_node = 1 -> None, prev_none = None, level_size = 1, i = 0







2) 

				1
			
			2         3

	   4       5  6       7 

	   Queue = [3], current_node = 2 -> None, prev_none = None, level_size = 2, i = 0


	   			1
			
			2         3

	   4       5  6       7 

	   Queue = [3, 4, 5], current_node = 2 -> None, prev_none = None, level_size = 2, i = 0


	   			1
			
			2         3

	   4       5  6       7 

	   Queue = [4, 5], current_node = 3 -> None, prev_none = 2 -> None, level_size = 2, i = 1


	             1
			
			2   ->      3

	   4       5   6       7 

	   Queue = [4, 5, 6, 7], current_node = 3 -> None, prev_none = 2 -> None, level_size = 2, i = 1


3) 

				1
			
			2   ->      3

	   4       5   6       7 

	   Queue = [4, 5, 6, 7], current_node = 3 -> None, prev_none = None, level_size = 3, i = 0

				


Complexity:
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
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " --> ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        prev_node = None

        for i in range(level_size):
            if i >= 1:
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
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()
main()