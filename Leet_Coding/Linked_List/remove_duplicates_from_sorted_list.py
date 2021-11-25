"""
Explanation:
-----------
deleteDuplicates1:
    Uses sentinel node and 'prev' pointer

deleteDuplicates2:
    Does the same job using a single pointer 'current'

Complexity:
----------
deleteDuplicates1
    Time: O(N)
    Space: O(1)

deleteDuplicates2:
    Time: O(N)
    Space: O(1)
"""
class Solution:
    def deleteDuplicates1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-101)
        sentinel.next = head
        prev, current = sentinel, head
        while current:
            if prev.val == current.val:
                prev.next = current.next
            else:
                prev = current    
            current = current.next

        return sentinel.next
    
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current = current.next.next
            else:
                current = current.next

        return head