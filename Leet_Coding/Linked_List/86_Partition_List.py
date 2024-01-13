"""
Complexity:
----------
Time: O(N)
Space: O(1)

"""
class Solution(object):
    def partition(self, head, x):
        if not head:
            return None
        after = after_head = ListNode(0)
        before = before_head = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next