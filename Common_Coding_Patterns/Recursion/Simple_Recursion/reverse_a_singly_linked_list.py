class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        return self.reverse_list_recursive(None, head, None)

    def reverse_list_recursive(self, prev_node, current_node, next_node):
        if current_node is None:
            return prev_node

        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

        return self.reverse_list_recursive(prev_node, current_node, next_node)