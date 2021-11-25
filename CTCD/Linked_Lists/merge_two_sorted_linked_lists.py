"""
Complexity:
----------
Time: O(M + N)
Space: O(1) since no recursion employed, we're just using one constant sentinel node.

"""
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode(-1)
        prev = pre_head
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 or l2

        return pre_head.next