"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        current_node = head
        last_m_node = head
        
        while current_node is not None:
            m_count = m
            n_count = n
            while current_node and m_count != 0:
                last_m_node = current_node
                current_node = current_node.next
                m_count -= 1

            while current_node and n_count != 0:
                current_node = current_node.next
                n_count -= 1

            last_m_node.next = current_node

        return head