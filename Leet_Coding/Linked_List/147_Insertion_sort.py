"""
Complexity:
----------
Time: O(N^2)
Space: O(1)
"""
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        prev = dummy
        current = head
        while current:
            next = current.next
            prev = dummy
            while prev.next and prev.next.val <= current.val:
                prev = prev.next

            current.next = prev.next
            prev.next = current
            current = next
            

        return dummy.next