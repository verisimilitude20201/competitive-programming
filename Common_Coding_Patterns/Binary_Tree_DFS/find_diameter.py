"""
Problem
-------
Given a binary tree, find the length of its diameter. 
The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Example:
-------
                    1

             2             3

             4         5        6

      Output = 5, Longest Diameter = [4, 2, 1, 3, 6]

Approach:
--------
1)  self.treeDiameter = 0


0.1 calculate_height(1)     # Node 1 - Root node
    --------------------------------------------

    leftTreeHeight = calculate_height(2)
    rightTreeHeight = rightTreeHeight = [Placeholder call for 1's right node]

0.2 calculate_height(2)     # Node 1's left child
    ---------------------------------------------
    leftTreeHeight = leftTreeHeight = calculate_height(4)
    rightTreeHeight = [Placeholder call for 2's right node]

0.3 calculate_height(4) # Node 2's left child
    -----------------------------------------
    leftTreeHeight = calculate_height(None)
    rightTreeHeight = [Placeholder call for 4's right node]

0.4 calculate_height(None) # Node 4's left child
    --------------------------------------------
    # 0 is returned since node 4 does not have left child


2) 0.4 stack frame is popped off

0.1 calculate_height(1)     # Node 1 - Root node
    --------------------------------------------

    leftTreeHeight = calculate_height(2)
    rightTreeHeight = rightTreeHeight = [Placeholder call for 1's right node]

0.2 calculate_height(2)     # Node 1's left child
    ---------------------------------------------
    leftTreeHeight = leftTreeHeight = calculate_height(4)
    rightTreeHeight = [Placeholder call for 2's right node]

0.3 calculate_height(4) # Node 2's left child
    -----------------------------------------
    leftTreeHeight = 0
    rightTreeHeight = calculate_height(None)

0.4  calculate_height(None) # Node 4's right child
    --------------------------------------------
    # 0 is returned since node 4 does not have right child


3) 0.4 stack frame is popped off

 0.1 calculate_height(1)     # Node 1 - Root node
    --------------------------------------------

    leftTreeHeight = calculate_height(2)
    rightTreeHeight = rightTreeHeight = [Placeholder call for 1's right node]

0.2 calculate_height(2)     # Node 1's left child
    ---------------------------------------------
    leftTreeHeight = leftTreeHeight = calculate_height(4)
    rightTreeHeight = [Placeholder call for 2's right node]

0.3 calculate_height(4) # Node 2's left child
    -----------------------------------------
    leftTreeHeight = 0
    rightTreeHeight = 0
    diameter = leftTreeHeight + rightTreeHeight + 1
    treeDiameter = max(tree_diameter, diameter) = max(0, 1) = 1
    return max(leftTreeHeight, rightTreeHeight) + 1


4) Stack frame 0.3 popped off


0.1 calculate_height(1)     # Node 1 - Root node
    --------------------------------------------

    leftTreeHeight = calculate_height(2)
    rightTreeHeight = rightTreeHeight = [Placeholder call for 1's right node]

0.2 calculate_height(2)     # Node 1's left child
    ---------------------------------------------
    leftTreeHeight = 1
    rightTreeHeight = calculate_height(None)


0.3 calculate_height(None)     # Node 2's right child
    # 0 is returned since node 4 does not have right child


5) 0.3 stack frame is popped off

0.1 calculate_height(1)     # Node 1 - Root node
    --------------------------------------------

    leftTreeHeight = calculate_height(2)
    rightTreeHeight = rightTreeHeight = [Placeholder call for 1's right node]

0.2 calculate_height(2)     # Node 1's left child
    ---------------------------------------------
    leftTreeHeight = 1
    rightTreeHeight = 0
    diameter = leftTreeHeight + rightTreeHeight + 1
    treeDiameter = max(tree_diameter, diameter) = max(1, 2) = 2
    return max(1, 0) + 1 ~ 2



6) Stack frame 0.2 popped off

0.1 calculate_height(1)     # Node 1 - Root node
    --------------------------------------------

    leftTreeHeight = 2
    rightTreeHeight = calculate_height(3)

0.2 calculate_height(3)   # Node 1's right child
    --------------------------------------------
    leftTreeHeight = calculate_height(5)
    rightTreeHeight =  [Placeholder call for 3's right node]

0.3 calculate_height(5)   # Node 3's left child
    -------------------------------------------
    leftTreeHeight = calculate_height(None)  # Because 5 is a leaf node
    rightTreeHeight =  [Placeholder call for 5's right node]


0.4 calculate_height(None)   # Node 5's left child
    ----------------------------------------------
    # Return 0


7) Stack-frame 0.4 for is popped off and pushed and popped once agian for 5's right node

0.1 calculate_height(1)     # Node 1 - Root node
    --------------------------------------------

    leftTreeHeight = 2
    rightTreeHeight = calculate_height(3)

0.2 calculate_height(3)   # Node 1's right child
    --------------------------------------------
    leftTreeHeight = calculate_height(5)
    rightTreeHeight =  [Placeholder call for 3's right node]

0.3 calculate_height(5)   # Node 3's left child
    -------------------------------------------
    leftTreeHeight  = 0
    rightTreeHeight = 0
    diameter = leftTreeHeight + rightTreeHeight + 1
    treeDiameter = max(2, 1) = max(1, 2) = 2
    return max(0, 0) + 1 ~ 1


8) Stack frame 0.3 is popped off. In a similar manner,  height of 3's right node is computed and is 1

  0.1 calculate_height(1)     # Node 1 - Root node
    --------------------------------------------

    leftTreeHeight = 2
    rightTreeHeight = calculate_height(3)

 0.2 calculate_height(3)   # Node 1's right child
    --------------------------------------------
    leftTreeHeight = 1
    rightTreeHeight = 1
    diameter = leftTreeHeight + rightTreeHeight + 1
    treeDiameter = max(2, 2) = max(2, 2) = 2
    return max(0, 0) + 1 ~ 2

9) Stack frame 0.3 is popped


0.1 calculate_height(1)     # Node 1 - Root node
    --------------------------------------------

    leftTreeHeight = 2
    rightTreeHeight = 2 
    diameter = 2 + 2 + 1
    treeDiameter = max(2, 5) = max(2, 5) = 5
    return max(0, 0) + 1 ~ 2

10) Stack frame 0.1 is popped and treeDiameter = 5


Complexity:
---------
Time: O(N) We visit all nodes
Space: O(log h) Where h is the maximum height of the tree. Worst case it would be O(N) if each node has one child.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeDiameter:

    def __init__(self):
        self.tree_diameter = 0

    def find_diameter(self, current_node):
        self.calculate_height(current_node)
        return self.tree_diameter

    def calculate_height(self, current_node):
        if current_node is None:
            return 0
        left_subtree_height = self.calculate_height(current_node.left)
        right_subtree_height = self.calculate_height(current_node.right)
        if left_subtree_height is not None and right_subtree_height is not None:
            diameter = left_subtree_height + right_subtree_height + 1
            self.tree_diameter = max(diameter, self.tree_diameter)

        return max(left_subtree_height, right_subtree_height) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()
