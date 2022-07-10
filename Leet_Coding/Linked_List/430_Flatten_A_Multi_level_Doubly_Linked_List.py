"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        pseudo_head = Node(None, None, head, None)
        self.flatten_recursively(pseudo_head, head)
        pseudo_head.next.prev = None
        
        return pseudo_head.next
    
    def flatten_recursively(prev: 'Optional[Node]', current: 'Optional[Node]') -> 'Optional[Node]':
        if not current:
            return prev
        current.prev = prev
        prev.next = current
        
        temp_next = current.next
        tail = self.flatten_recursively(current, current.child)
        current.child = None
        return self.flatten_recursively(tail, temp_next)