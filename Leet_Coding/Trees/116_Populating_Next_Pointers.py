"""
Complexity:
----------
Time: O(N)
Space: O(N) Since it's a perfect binary tree, and maximum number of nodes at a given time in Queue is equal to the number of nodes at the last level in the 
Tree
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        Q = deque([root])
        while len(Q):
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                if i < size - 1:
                    node.next = Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        return root