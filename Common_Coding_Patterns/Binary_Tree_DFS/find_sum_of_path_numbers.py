"""
Problem:
-------
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. 
Find the total sum of all the numbers represented by all paths.

Example:
-------
            1   

         7      9

              2     9


Sum = 17 + 192 + 199 = 408


Approach
-------
DFS

0)           1   

         7      9

              2     9


Sum = 17 + 192 + 199

find_root_to_leaf_path_numbers(root, 0)


1) find_root_to_leaf_path_numbers(1, pathSum=0)     # For root node 1
   ------------------------------------------------------------------

   pathSum = 0 * 10 + 1 = 1
   find_root_to_leaf_path_numbers(7, 1)  +  find_root_to_leaf_path_numbers(9, 1)

  
  find_root_to_leaf_path_numbers(7, 1)     # For root node's node left child
  --------------------------------------------------------------------------
   pathSum = 1 * 10 + 7 = 17

   # 7 does not have a left child or right child, so pop the stack frame and return 17


   find_root_to_leaf_path_numbers(1, pathSum=0)     # For root node 1
   ------------------------------------------------------------------

   pathSum = 0 * 10 + 1 = 1
   17  +  find_root_to_leaf_path_numbers(9, 1)



2) find_root_to_leaf_path_numbers(9, 1) # Node 1's right child
   -----------------------------------------------------------
   path_sum = 1 * 10 + 9 = 19
   find_root_to_leaf_path_numbers(2, 19)  +  find_root_to_leaf_path_numbers(9, 19)

   find_root_to_leaf_path_numbers(2, 19) # Node 9's left child
   -----------------------------------------------------------
   path_sum = 19 * 10 + 2 = 192
   # Since 2 is a leaf node, so pop the stack frame and return 192

   find_root_to_leaf_path_numbers(9, 1) # Node 9's left child
   -----------------------------------------------------------
   path_sum = 1 * 10 + 9 = 19
   192 +  find_root_to_leaf_path_numbers(9, 19)


   find_root_to_leaf_path_numbers(9, 19) # Node 9's right child
   ------------------------------------------------------------
   path_sum = 19 * 10 + 9 = 199
   # Since 9 is a leaf node, so pop the stack frame and return 199


   find_root_to_leaf_path_numbers(9, 1) # Node 9's left child
   -----------------------------------------------------------
   path_sum = 1 * 10 + 9 = 19
   391

   Pop all stack frames and return 391
   
   


3)  find_root_to_leaf_path_numbers(1, pathSum=0)     # For root node 1
   ------------------------------------------------------------------

   pathSum = 0 * 10 + 1 = 1
   17  +  391 = 408




Complexity:
----------
Time: O(N) Because it needs to visit each node
Space: O(N) Because it will have N stack frames corresponding to N recursive calls on stack
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_sum_of_path_numbers(root):
    return find_root_to_leaf_path_numbers(root, 0)


def find_root_to_leaf_path_numbers(current_node, path_sum):
    if current_node is None:
        return 0
    path_sum = path_sum * 10 + current_node.value

    if current_node.left is None and current_node.right is None:
        return path_sum

    return find_root_to_leaf_path_numbers(current_node.left, path_sum) + find_root_to_leaf_path_numbers(
        current_node.right, path_sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
