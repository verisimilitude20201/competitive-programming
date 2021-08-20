"""
Explanation:
-----------
Simply reverse the list and compare each node

Complexity:
----------
Time: O(N)
Space: O(N)
"""

from base.base_linked_list import SingleLinkedList


def is_palindrom(l1):
    reversed_head = reverse_list(l1.head)
    return is_equal(l1.head, reversed_head)


def reverse_list(node):
    new_head = None
    while node:
        new_node = SingleLinkedList.Node(node.data)
        new_node.next = new_head
        new_head = new_node
        node = node.next

    return new_head


def is_equal(node1, node2):
    while node1 is not None and node2 is not None:
        if node1.data != node2.data:
            return False
        node1 = node1.next
        node2 = node2.next

    return node1 is None and node2 is None


if __name__ == '__main__':
    l1 = SingleLinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(1)

    print(is_palindrom(l1))
