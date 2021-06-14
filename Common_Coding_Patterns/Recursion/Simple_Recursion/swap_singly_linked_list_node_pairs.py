class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution: 
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        current_node = head
        self.swap_pairs_recursive(current_node)
        return head

    def swap_pairs_recursive(self, node: ListNode):
        if node is None or node.next is None: 
            return

        node.val, node.next.val = node.next.val, node.val
        self.swap_pairs_recursive(node.next.next)