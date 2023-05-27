"""
Complexity:
---------
Time: O(N)
Space: O(N)
"""
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.add_parent_pointers(root, None)
        Q = deque([target])
        seen = set()
        seen.add(target)
        distance = 0
        while len(Q) and distance < k:
            current_len = len(Q)
            for _ in range(current_len):
                node = Q.popleft()
                for temp in [node.left, node.right, node.parent]:
                    if temp and temp not in seen:
                        Q.append(temp)
                        seen.add(temp)
            
            distance += 1
        
        return [node.val for node in Q]
    
    
    def add_parent_pointers(self, node: TreeNode, parent: Optional[TreeNode]):
        if not node:
            return
        
        node.parent = parent
        self.add_parent_pointers(node.left, node)
        self.add_parent_pointers(node.right, node)