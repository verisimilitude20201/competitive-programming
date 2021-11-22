"""
Complexity:
----------
    hasCycle1
        Time: O(N)
        Space: O(N)
    
    hasCycle2:
        Time: O(N)
        Space: O(1)
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        node_seen = set()
        node = head
        while node:
            if node in node_seen:
                return True
            node_seen.add(node)
            node = node.next
        
        return False
    
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head.next
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        
        return True