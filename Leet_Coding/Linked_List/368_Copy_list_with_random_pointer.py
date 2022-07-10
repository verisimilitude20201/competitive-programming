"""
Complexity:
----------
Solution 1 -->
Time: O(N)
Space: O(N)

Solution 2 --->

Time: O(N)
Space: O(N)

Soltion 3 -->
Time: O(N)
Space: O(1)

"""
class Solution1:
    def __init__(self):
        self._visited_nodes = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        node = Node(head.val, None, None)
        if head in self._visited_nodes:
            return self._visited_nodes[head]
        
        self._visited_nodes[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node


class Solution2:
    def __init__(self):
        self._visited = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        old_node = head
        new_node = Node(old_node.val, None, None)
        self._visited[old_node] = new_node
        while old_node:
            next_node = self._get_node(old_node.next)
            random_node = self._get_node(old_node.random)
            new_node.next = next_node
            new_node.random = random_node
            old_node = old_node.next
            new_node = new_node.next
        return self._visited[head]
               
    
    def _get_node(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if not node:
            return None
        if node in self._visited:
            return self._visited[node]
        self._visited[node] = Node(node.val, None, None)
        return self._visited[node]

class Solution3:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        ptr = head
        while ptr:
            node = Node(ptr.val, None, None)
            node.next = ptr.next
            ptr.next = node
            ptr = node.next
        ptr1 = head
        while ptr1:
            ptr1.next.random = ptr1.random.next if ptr1.random else None
            ptr1 = ptr1.next.next
        
        ptr1 = head
        new_head, ptr2 = head.next, head.next
        while ptr1:
            ptr1.next = ptr1.next.next
            ptr1 = ptr1.next
            ptr2.next = ptr2.next.next if ptr2.next else None
            ptr2 = ptr2.next
        
        return new_head