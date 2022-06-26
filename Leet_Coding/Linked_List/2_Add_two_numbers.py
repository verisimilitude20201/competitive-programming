"""
Explanation:
-----------
2 -> 4 -> 3 -> 5 -> 5
                    p
L1          

5 -> 6 -> 4 -> None
               q
L2



carry = 0, x = 2 , y = 5 , total  = 7

0 -> 7 -> 0 -> None
DH
          C
     
carry = 1, x = 3 , y = 4 , total  = 8
         
0 -> 7 -> 0 -> 8 -> None
DH
               C

carry = 0, x = 5 , y = 0 , total  = 5
         
0 -> 7 -> 0 -> 8 ->  5 -> None
DH
                     C


carry = 0, x = 5 , y = 0 , total  = 5
         
0 -> 7 -> 0 -> 8 ->  5 ->  5 -> None
DH
                           C

Complexity:
----------
Time: O(max(M, N))
Space: O(max(M, N) + 1)
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        total, carry = 0, 0
        dummy_head = ListNode(0)
        current = dummy_head
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            total = x + y + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
            current = current.next
        if carry > 0:
            current.next = ListNode(1)