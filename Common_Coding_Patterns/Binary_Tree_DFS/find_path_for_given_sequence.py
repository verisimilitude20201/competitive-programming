"""
Problem
-------
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree

Example
-------
        1
    7      9
        9    2

   [1, 7, 0] is not present
   [1, 9, 9] is present     

Approach
-------
DFS of the binary tree

1. Given sequence is not traceable in the root to leaf node traversal for the below conditions
  a. Leaf node has been reached and still the sequence is not found 
  b. Sequence index >= lenth of the sequence

2. Sequence is found if a root node is reached and the sequence index = len(sequence) - 1

Complexity:
----------
Time: O(N)
Space: O(N)
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_path_for_given_sequence(root, sequence):
    if not root:
        return len(sequence) == 0

    return is_sequence_present_in_tree(root, sequence, 0)


def is_sequence_present_in_tree(current_node, sequence, sequence_index):
    if current_node is None:
        return False

    if sequence_index >= len(sequence) or sequence[sequence_index] != current_node.value:
        return False

    if current_node.left is None and current_node.right is None and sequence_index == len(sequence) - 1:
        return True

    return is_sequence_present_in_tree(current_node.left, sequence, sequence_index + 1) or is_sequence_present_in_tree(
        current_node.right, sequence, sequence_index + 1)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path_for_given_sequence(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path_for_given_sequence(root, [1, 1, 6])))


main()
