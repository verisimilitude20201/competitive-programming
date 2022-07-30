"""
Explanation:
----------
Just copy the value of the next node into the current node and change it's next pointer to pointer to the node after the next

Complexity:
----------
Time: O(1)
Space: O(1)

"""
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next