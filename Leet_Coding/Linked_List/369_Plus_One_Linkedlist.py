"""
Explanation
----------
Case 1: No 9 in any place
------
0 ->   1 -> 3 -> 1
S                   NN
                 H


Case 2: 9 not in units place
0 ->   1 -> 9 -> 3
S                     H                  
                 NN       
                 

Case 3: 9  in units place
0 ->   1 -> 9 -> 9
S                     
NN     H

Case 4: all 9s
1 ->   9 -> 0 -> 0
S                     
NN                  H
                      
Case 5: Empty list

0       -> None
NN          H
S



Complexity:
----------
Time: O(N)
Space: O(1)

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sentinal = ListNode(0)
        sentinal.next = head
        not_nine = sentinal
        
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next
        
        not_nine.val += 1
        not_nine = not_nine.next
        
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next
        
        return sentinal if sentinal.val else sentinal.next