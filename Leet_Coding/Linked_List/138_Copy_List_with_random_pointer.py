"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def __init__(self):
        self.visited_node = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        if head in self.visited_node:
            return self.visited_node[head]

        node = Node(head.val, None, None)
        self.visited_node[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution3:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # Weave next pointers
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        # Link Random pointers
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        # Unweave list & return cloned one
        ptr_new = head.next
        ptr_old = head
        head_new = head.next
        while ptr_old:
            ptr_old.next = ptr_old.next.next
            ptr_new.next = ptr_new.next.next if ptr_new.next else None
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next

        return head_new