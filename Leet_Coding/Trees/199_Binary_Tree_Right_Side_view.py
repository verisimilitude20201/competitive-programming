"""
Complexity:
---------
Time: O(N)
Space: O(2^D) Where D is the depth of the binary tree
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    
            return []
        Q = deque([root])
        right_side_view = []
        while len(Q):
            right_side_view.append(Q[-1].val)
            for _ in range(len(Q)):
                node = Q.popleft()
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        return right_side_view