"""
Problem:
-------
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.


Example:
-------

                1
			
			7           9

	    4        5   2      7


     Total = 12
	 all_paths[[1, 7, 4], [1, 9, 2]]

Approach:
--------
DFS

0)
				 1
			
			7           9

	    4        5   2      7


     Total = 12
	 all_paths[[1, 7, 4], [1, 9, 2]]

	 find_paths_recursive(currentNode, required_sum, currentPath, allPaths):


1) Recursion Trace



find_paths_recursive(1, 12, [], []) ---> find_paths_recursive(1, 12, [1], [])        		   # 1 Root node
find_paths_recursive(7, 11, [1], []) ---> find_paths_recursive(7, 11, [1, 7], [])              # 1's left node 7 
find_paths_recursive(4, 4, [1, 7], []) ---> find_paths_recursive(4, 4, [1, 7, 4], [[1, 7, 4]]) # 7's left node 4


2) Back-track to 7

find_paths_recursive(7, 11, [1], [[1, 7, 4]]) ---> find_paths_recursive(7, 11, [1, 7], [[1, 7, 4]])              # 1's left node 7
find_paths_recursive(5, 6, [1, 7], [[1, 7, 4]]) --> find_paths_recursive(5, 6, [1, 7, 5], [[1, 7, 4]])                                                                   # 7's right node 5


3) Back-track to 1


Complexity:
----------
Time: O(N^2) We traverse each node once and once we find correct path, we convert it into a list and append it to all_paths
Space: O(N * log N)
    We have 7 nodes in the above example tree.
    Total root-to-leaf paths <= Number of leaves
    There cannot be more than ((N + 1) / 2) leaves in a binary tree.
    Number of elements in all_path can be O(N)
    Maximum height of Binary tree is O(log N)
    Each path can have a total of O(log N) nodes
    Therefore, the size of all_paths can be  O(N * log N)

"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_paths(root, total):
    all_paths = []
    find_all_paths_for_sum(root, total, [], all_paths)

    return all_paths


def find_all_paths_for_sum(root, total, current_path, all_paths):
    if root is None:
        return
    current_path.append(root.value)
    if root.value == total and root.left is None and root.right is None:
        all_paths.append(list(current_path))
    else:
        find_all_paths_for_sum(root.left, total - root.value, current_path, all_paths)
        find_all_paths_for_sum(root.right, total - root.value, current_path, all_paths)
    del current_path[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
