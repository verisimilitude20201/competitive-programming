"""
Complexity:
----------
Time: O(N * 2^d)
Space: O(2^d)
"""
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        largest = []
        Q = deque([root])
        while len(Q):
            max_num = -math.inf
            for _ in range(len(Q)):
                node = Q.popleft()
                max_num = max(node.val, max_num)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            largest.append(max_num)
        return largest