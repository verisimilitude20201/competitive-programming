"""
Complexity
---------
Solution 1
---------
Time: O(N)
Space: O(N)

Solution 2
----------
Time: O(N)
Space: O(1)

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second

class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        dummy = head.next
        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head
            next_node = head.next.next
            head.next.next = head
            head.next = next_node
            head = next_node
        
        return dummy
        