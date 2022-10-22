"""
Complexity:
---------
Time: O(N)
Space: O(N)
"""
class Solution:
    def __init__(self):
        self.stop = False
        self.left = None
        
    
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head:
            return None
        self.left = head
        self.reverse_between_range(head, m, n)
        
        return head
        
    
    def reverse_between_range(self, right: Optional[ListNode], m: int, n: int):
        if n == 1:
            return
        
        right = right.next
        
        if m > 1:
            self.left = self.left.next
        
        self.reverse_between_range(right, m - 1, n - 1)
        
        if right == self.left or right.next == self.left:
            self.stop = True
            return
        
        if not self.stop:
            self.left.val, right.val = right.val, self.left.val
            self.left = self.left.next