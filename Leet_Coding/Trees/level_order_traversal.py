"""
Complexity:
----------
Both iterative and recursive
Time: O(N)
Space: O(N)

"""
class Solution:
    def levelOrderRecursive(self, root):
        levels = []
        
        def bfs(root, level):
            if not root:
                return
            if len(levels) == level:
                levels.append([])
            levels[level].append(root.val)
            if root.left:
                bfs(root.left, level + 1)
            if root.right:
                bfs(root.right, level + 1)
          
        if root:
            bfs(root, 0)
        
        return levels
    
    def levelOrderIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        level = 0
        levels = []
        q = deque()
        q.append(root)
        while q:
            levels.append([])
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return levels