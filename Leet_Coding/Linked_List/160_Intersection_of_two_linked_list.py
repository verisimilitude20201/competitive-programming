"""
Complexity:
----------
Solution 1 -> BruteForce
-----------------------
Time: O(M * N)
Space: O(1)

Solution2 --> 
--------------
Time: O(M + N)
Space: O(M + N)

Solution 3
----------
Time: O(M + N)
Space: O(1)
"""
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a:
            b = headA
            while b:
                if a == b:
                   return a
                b = b.next
            a = a.next
        return None

class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        a = headA
        while a:
            visited.add(a)
            a = a.next
        b = headB
        while b:
            if b in visited:
                return b
            visited.add(b)
            b = b.next
        return None

class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        PA = headA
        PB = headB
        while PA != PB:
           PA = headB if PA is None else PA.next
           PB = headA if PB is None else PB.next
        return PA