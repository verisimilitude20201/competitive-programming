"""
Problem
-------
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Example:
-------
    12             ---> root

  7     1        

  9   10  5  
  
  Result = [[12], [7, 1], [9, 10, 5]]

Approach:
--------
BFS using a Doubly-Ended Queue (Even a Queue is also fine here)


0)  
    12             ---> root

  7     1        

  9   10  5  
  
  Queue = [] 
  Result = []

1) Add root node to queue

Queue = [12]
levelNodes = 1

2) while Queue is empty, add nodes to result

	i) levelNodes = 0, pop 12 from Queue

 	Result = [[12]]


ii) levelNodes = 1, Queue = [], break out

3) Add 12's children to queue

	Queue = [7, 1]
	levelNodes = 2

4) While queue is empty, 

	 i) levelNodes = 0, pop 7 from Queue

	 Result = [[12], [7]]
	 Add 7's children to queue

	 Queue = [1, 9]

	 ii) levelNodes = 1, pop 1 from Queue

	 	Result = [[12], [7, 1]]

	 	Add 1's children to Queue
	 	Queue = [9, 10, 5]

	 iii) levelNodes = 2, break out

	   Queue = [9, 10, 5]

5) while Queue is empty

   i)  levelNodes = 0, pop 9 from queue

        Result = [[12], [7, 1], [9]]

        9 does not have any children
        Queue = [10, 5]

   ii)  levelNodes = 1, pop 10 from queue
   		Result = [[12], [7, 1], [9, 10]]
   		Queue = [5]


   iii) levelNodes = 1, pop 10 from queue
   		Result = [[12], [7, 1], [9, 10, 5]]
   		Queue = [5]
    

 6) Result = [[12], [7, 1], [9, 10, 5]]


Complexity
---------
Time: O(N) N is number of nodes in tree
Space: O(N) We require M-size queue to hold nodes on any given level. Final size of the result is O(N). Since N >= M, we consider complexity as O(N)
"""

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def traverse_binary_tree_level_wise(root):
    result = []
    if root is None:
        return []

    q_deque = deque()
    q_deque.append(root)
    while q_deque:
        level_size = len(q_deque)
        current_level_node_value = []
        for i in range(level_size):
            current_node = q_deque.popleft()
            current_level_node_value.append(current_node.value)
            if current_node.left is not None:
                q_deque.append(current_node.left)
            if current_node.right is not None:
                q_deque.append(current_node.right)
        result.append(current_level_node_value)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse_binary_tree_level_wise(root)))


main()
