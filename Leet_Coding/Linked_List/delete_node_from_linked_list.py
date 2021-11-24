"""
Complexity:
----------
    Time: O(N)
    Space: O(1)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        sentinal = ListNode(-1)
        sentinal.next = head
        prev, current = sentinal, head

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        

        return sentinal.next