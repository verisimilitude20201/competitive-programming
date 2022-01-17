"""
Explanation:
-----------
1. Uses a Set to store the value of all nodes of BST. Does not use BST property
2. Uses a set to store a level-ordered traversal of a BST. Again does'nt use BST property.
3. Create a sorted list by traversing the BST in-order. Then, take two pointers l and r. If the total at 
those indexes equals required sum, return True. If the total is less than the required sum, increment l
else increment r


Complexity:
---------
findTarget1/findTarget2/findTarget3
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def findTarget1(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        vals = set()
        return self.search1(root, vals, k)
        
    def search1(self, root: TreeNode, vals, k: int) -> bool:
        if root is None:
            return False
        if (k - root.val) in vals:
            return True
        vals.add(root.val)
        return self.search(root.left, vals, k) or self.search(root.right, vals, k)
    
    def findTarget2(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        Q = deque()
        Q.append(root)
        vals = set()
        while len(Q):
            node = Q.popleft()
            if node:
                if (k - node.val) in vals:
                    return True
                vals.add(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return False
    
    def findTarget3(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        inorder = []
        self.traverseInOrder(root, inorder)
        l = 0
        r = len(inorder) - 1
        while l < r:
            req_sum = inorder[l] + inorder[r]
            if req_sum == k:
                return True
            elif req_sum < k:
                l += 1
            else:
                r -= 1

        return False

    def traverseInOrder(self, root: Optional[TreeNode], inorder) -> bool:
        if root is None:
            return
        self.traverseInOrder(root.left, inorder)
        inorder.append(root.val)
        self.traverseInOrder(root.right, inorder)