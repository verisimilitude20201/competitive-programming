"""
Problem
------
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

Example:
-------
                12
			
			7         1

	    9          10       5

        [12, 1, 10] is the desired path giving sum = 23
        [] is desired path giving sum = 16
Approach:
--------
Depth first search since we are going the find the path with the given sum.

0) has_path(12, 23)
1) has_path(7, 11) or has_path(root.right, sum - root.val)            # 12's left sub-tree
2) has_path(9, 4) or has_path(root.right, sum - root.val)             # 7's left sub-tree
3) has_path(None, -5) or has_path(root.right, sum - root.val)         # 9's left_sub-tree

   False or has_path(root.right, sum - root.val)                      # 9 is a leaf node and 9 does not have either left or right child

3) False # 9 is a leaf node and 9 does not have either left or right child
2) False # 9 is a leaf node and 9 does not have either left or right child
1) False # 7 does not have right child
0) has_path(12, 23)

1) has_path(1, 11) or has_path(root.right, sum - root.val)
2) has_path(10, 10) or has_path(root.right, sum - root.val) # we found the required sum 10, 10


Complexity:
---------
Time: O(N)
Space: O(N) Worst case will happen if every node has one child
"""

