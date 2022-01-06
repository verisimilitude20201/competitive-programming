"""
Complexity:
----------
For both iterative and recursive.

Time: O(N)
Space: O(N)

"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricRecursive(root, root)

    def isSymmetricRecursive(self, T1: Optional[TreeNode], T2: Optional[TreeNode]) -> bool:
        if T1 is None and T2 is None:
            return True

        if T1 is None or T2 is None:
            return False

        return T1.val == T2.val and self.isSymmetricRecursive(T1.left, T2.right) and self.isSymmetricRecursive(T1.right,
                                                                                                               T2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.appendleft(root)
        q.appendleft(root)
        while len(q):
            t1 = q.pop()
            t2 = q.pop()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            q.appendleft(t1.left)
            q.appendleft(t2.right)
            q.appendleft(t1.right)
            q.appendleft(t2.left)
        return True