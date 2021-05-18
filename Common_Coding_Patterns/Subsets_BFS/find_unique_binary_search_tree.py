"""
Problem:
-------
Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?



Example:
-------

Input: 2
Output: List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2

            1                          2
                            &           
        2                           1 

Approach:
--------
Similar to generate valid parenthesis approach.

Complexity:
----------
Time: O(N * 2 ^ N)
Space: O(N * 2 ^ N)

"""

class BST:
    def __init__(self, value):
        self._value = value
        self.left = None
        self.right = None


def unique_binary_trees(n):
    if n <= 0:
        return []

    return unique_binary_search_trees_recursive(1, n)


def unique_binary_search_trees_recursive(start_val, end_val):
    result = []
    if start_val > end_val:
        result.append(None)
        return result

    for i in range(start_val, end_val + 1):
        left_sub_tree = unique_binary_search_trees_recursive(start_val, i - 1)
        right_sub_tree = unique_binary_search_trees_recursive(i + 1, end_val)
        root = BST(i)
        for left_tree in left_sub_tree:
            for right_tree in right_sub_tree:
                root.left = left_tree
                root.right = right_tree
                result.append(root)
    return result


def main():
  print("Total trees: " + str(len(unique_binary_trees(2))))
  print("Total trees: " + str(len(unique_binary_trees(3))))


main()