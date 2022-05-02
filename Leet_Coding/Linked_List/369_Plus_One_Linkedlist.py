"""
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