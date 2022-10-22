"""
Complexity:
---------
Time: O(N)
Space: O(1)

"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head.next.next is None:
            return head.val + head.next.val
        
        middle_node = self.get_middle_node(head)
        reversed_middle_node = self.reverse_second_half(middle_node)
        max_val = 0
        while reversed_middle_node:
            max_val = max(max_val, reversed_middle_node.val + head.val)
            head = head.next
            reversed_middle_node = reversed_middle_node.next
        
        return max_val
    
    def get_middle_node(self, node: Optional[ListNode]) -> 'ListNode':
        fast = node
        slow = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverse_second_half(self, middle_node: Optional[ListNode]) -> 'ListNode':
        prev = None
        current = middle_node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node