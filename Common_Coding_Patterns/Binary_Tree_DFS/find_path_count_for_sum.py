"""
Problem:
-------
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. 
Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

Example:
-------
             1   

         7       9

      6    5   2     3


Required Sum = 12
 
3 Paths with sum 12 -> [1, 9, 2], [9, 3], [7, 5]

Approach:
--------
DFS to visit each node and path

0)           1   

         7       9

      6    5   2     3


Required Sum = 12
 
3 Paths with sum 12 -> [1, 9, 2], [9, 3], [7, 5]


1) 
 

	0.1 find_path_count_for_sum(1, 12, 0, [])
	    -------------------------------------
	    current_path = [1]
	    find_path_count_for_sum(7, 12, 0, [1])   # 1's left child
	    [Placeholder for call to 1's right child]

	0.2 find_path_count_for_sum(7, 12, 0, [1])   # 1's left child
	    ---------------------------------------------------------
	    current_path = [1, 7]
	    find_path_count_for_sum(6, 12, 0, [1, 7])   # 7's left child
	    [Placeholder for call to 7's right child]

	0.3  find_path_count_for_sum(6, 12, 0, [1, 7])   # 7's left child
	     -----------------------------------------------------------
	     current_path = [1, 7, 6]
	     # 6 is a leaf node
	     # Find the reverse sum (from leaf to root) of all array elements of current path. 
	     # It does not equal 12
	     # Back-track to 7 by removing 12

2) 0.3 stack frame popped

    0.1 find_path_count_for_sum(1, 12, 0, [])
	    -------------------------------------
	    current_path = [1]
	    find_path_count_for_sum(7, 12, 0, [1])   # 1's left child
	    [Placeholder for call to 1's right child]

	0.2 find_path_count_for_sum(7, 12, 0, [1])   # 1's left child
	    ---------------------------------------------------------
	    current_path = [1, 7]
	    # Path count for [1, 7, 6] is 0
	    find_path_count_for_sum(5, 12, 0, [1, 7])   # 7's right child

	0.3 find_path_count_for_sum(5, 12, 0, [1, 7])   # 7's right child
	    -------------------------------------------------------------
	    current_path = [1, 7, 5]
	    # Path count for [7, 5] is 12
	    # Increment path_count to 1
	    # Backtrack to 7

3) 0.3 stack frame popped and path_count is set to 1

   0.1 find_path_count_for_sum(1, 12, 0, [])
	    -------------------------------------
	    current_path = [1]
	    find_path_count_for_sum(7, 12, 0, [1])   # 1's left child
	    [Placeholder for call to 1's right child]

   0.2 find_path_count_for_sum(7, 12, 0, [1])   # 1's left child
	    ---------------------------------------------------------
	    current_path = [1, 7]
	    # Path count for [1, 7, 6] is 0
	    # Path count for [5, 7] is 1
	    # Back-track to 1

4) 0.2 stack frame popped and path_count is 1
   We now process the right sub-tree of the root node 1
   
   0.1 find_path_count_for_sum(1, 12, 0, [])
	    -------------------------------------
	    current_path = [1]
	    # 1's left tree completely processed - path_count = 1
	    find_path_count_for_sum(9, 12, 1, [1])   # 1's right child

   0.2 find_path_count_for_sum(9, 12, 1, [1])   # 1's right child
       ----------------------------------------------------------
       current_path = [1, 9]
       find_path_count_for_sum(2, 12, 1, [1, 9])   # 9's left child
       [Place holder call for 9's right child]

   0.3 find_path_count_for_sum(2, 12, 1, [1, 9])   # 9's left child
       ------------------------------------------------------------
       current_path = [1, 9, 2]
       # 2 is leaf node
       # Path sum of [1, 9, 2] is 12
       # Increment path_count to 2
       # Back-track to 9 
       # Return path_count as 2

5) 0.3 stack frame popped

   0.1 find_path_count_for_sum(1, 12, 0, [])
	    -------------------------------------
	    current_path = [1]
	    # 1's left tree completely processed - path_count = 1
	    find_path_count_for_sum(9, 12, 1, [1])   # 1's right child

   0.2 find_path_count_for_sum(9, 12, 1, [1])   # 1's right child
       ----------------------------------------------------------
       current_path = [1, 9]
       # path_count is 2   # 9's left child
       find_path_count_for_sum(3, 12, 2, [1, 9])   # 9's right child

   0.3 find_path_count_for_sum(3, 12, 2, [1, 9])   # 9's right child
       -------------------------------------------------------------
       current_path = [1, 9, 3]
       # 3 is leaf node
       # Path sum of [9, 3] is 12
       # Increment path_count to 3
       # Back-track to 9 
       # Return path_count as 3

6) 0.3 stack frame popped and path_count 3 returned
   
   0.1 find_path_count_for_sum(1, 12, 0, [])
	    -------------------------------------
	    current_path = [1]
	    # 1's left tree completely processed - path_count = 1
	    find_path_count_for_sum(9, 12, 1, [1])   # 1's right child

   0.2 find_path_count_for_sum(9, 12, 1, [1])   # 1's right child
       ----------------------------------------------------------
       current_path = [1, 9]
       # path_count is 2  for 9's left child
       # Path count is 3  for 9's right child
       # Back track to 1
       # Return path_count as 3

 7) 0.2 stack frame popped and path_count 3 returned

    0.1 find_path_count_for_sum(1, 12, 0, [])
	    -------------------------------------
	    current_path = [1]
	    # 1's left tree completely processed - path_count = 1
	    # 1's right tree completely processed - path_count = 3
	    # Remove root node from current_path since all nodes processes

 8) Pop the stack frame 0.1 and return 3 as path_count

Complexity:
----------
Time: O(N * log N). Because we visit each node to find the current path and once a path is found, we take log N time to compute the sum. Length of the longest path is the height
of the binary tree which is log(N)
Space: O(log N). Worst case complexity will happen if each node has just one child so the stack frames would be O(N)

"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_paths_in_tree_for_sum(root, total):
    return find_path_count_for_sum(root, total, 0, [])


def find_path_count_for_sum(current_node, total, path_count, current_path):
    if current_node is None:
        return path_count

    current_path.append(current_node.value)
    if current_node.left is None and current_node.right is None:
        path_sum = 0
        for i in range(len(current_path) - 1, -1, -1):
            path_sum += current_path[i]
            if path_sum == total:
                path_count += 1
    else:
        path_count = find_path_count_for_sum(current_node.left, total, path_count, current_path)
        path_count = find_path_count_for_sum(current_node.right, total, path_count, current_path)

    del current_path[-1]
    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths_in_tree_for_sum(root, 11)))


main()
