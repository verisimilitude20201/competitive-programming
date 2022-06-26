"""
Explanation:
-----------
Solution1
---------
Time: O(N)
Space: O(N)

Solution 2
----------
Time: O(N)
Space: O(1)

"""
class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head
        while current:
            if current in visited:
                return current
            visited.add(current)
            current = current.next
        return None


class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        intersect = self.get_intersect_point(head)
        if not intersect:
            return None
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
    
    def get_intersect_point(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return slow
        return None