"""
Problem:
-------
Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.
Path may not necessarily pass through the root.

Example:
-------
             1

       2             3

    1      3     5         6

              7    8    9    10 

Path 1: [1, 2, 3] ~ 6
Path 2: [1, 2, 1, 3, 5, 7] ~ 19
Path 3: [7, 5, 3, 6, 9] ~ 29
Path 4: [8, 5, 3, 6, 9] ~ 31 

Output = 31


Approach
-------

1. At each node, compute the maximum sum of its left tree and right_tree. Add current node's value to it.
2. To find the maximum path sum = left sum + right sum + current value

Complexity:
----------
Time: O(N)
Space: O(log H) where H is maximum height of tree. Worst case, it can be O(N) if each node has one child only
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreePathSum:
    def __init__(self):
        self.max_tree_sum = -1

    def find_maximum_path_sum(self, current_node):
        self.calculate_recursive_sum(current_node)
        return self.max_tree_sum

    def calculate_recursive_sum(self, current_node):
        if current_node is None:
            return 0
        left_tree_sum = self.calculate_recursive_sum(current_node.left)
        right_tree_sum = self.calculate_recursive_sum(current_node.right)
        if left_tree_sum is not None and right_tree_sum is not None:
            left_tree_sum = max(left_tree_sum, 0)
            right_tree_sum = max(right_tree_sum, 0)
            sum_for_tree_rooted_at_current_node = left_tree_sum + right_tree_sum + current_node.value

            self.max_tree_sum = max(sum_for_tree_rooted_at_current_node, self.max_tree_sum)

        return max(left_tree_sum, right_tree_sum) + current_node.value


def main():
    maximumPathSum = TreePathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()
