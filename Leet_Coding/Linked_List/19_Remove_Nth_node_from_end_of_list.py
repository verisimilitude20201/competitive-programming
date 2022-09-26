"""
Explanation:
-----------
Solution 1 --> Two Pass
Time: O(N)
Space: O(1)

Solution 2 --> One Pass
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        current = dummy
        length -= n
        while length:
            current = current.next
            length -= 1
        current.next = current.next.next
        return dummy.next

class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n + 1):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return dummy.next
            
        