"""
Complexity:
----------
    reverseList1:
        Time: O(N)
        Space: O(1)

    reverseList2:
        Time: O(N)
        Space: O(N) Because we're pushing N function calls on Stack.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev, current = None, head
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev
    
    def reverseList1(head):
        if head is None or head.next is None:
            return head
        p = reverse(head.next)
        head.next.next = head
        head.next = None

        return p