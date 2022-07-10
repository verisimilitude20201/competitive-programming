"""
Complexity:
-----------

Solution 1
----------
Time: O(N * K)
Space: O(1)
"""
class Solution1:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        k %= length
        ptr = head
        val = ptr.val
        while k:
            while ptr.next is not None:
                ptr.next.val, val = val, ptr.next.val
                ptr = ptr.next
            head.val, val = val, head.val
            ptr = head
            val = head.val
            k -= 1
        
        return head