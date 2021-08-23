"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""

from base import SingleLinkedList


def get_node_at_start_of_cycle(head):
    fast = head
    slow = head
    while slow and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == '__main__':
    node_C = SingleLinkedList.Node("C")
    node_common = SingleLinkedList.Node("A")
    node_common.next = SingleLinkedList.Node("B")
    node_common.next.next = node_C
    node_common.next.next.next = SingleLinkedList.Node("D")
    node_common.next.next.next.next = SingleLinkedList.Node("E")
    node_common.next.next.next.next.next = node_C
    print(get_node_at_start_of_cycle(node_common))