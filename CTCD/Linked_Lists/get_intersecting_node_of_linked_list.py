"""
Explanation
----------

1. If two lists L1 and L2 don't have the same tail by reference, they don't intersect
2. Find the longer of the two lists
3. Get the Kth = abs(length1 - length2) of the longest list. Basically we skip K nodes so as to align the start node of the lists.
4. Loop through the second list and first list (from the Kth starting node) until they meet. 
5. The meeting point is the intersecting node.

Complexity:
----------
Time: O(M + N)
Space: O(1)

"""
from base import SingleLinkedList


def get_intersecting_node(l1, l2):
    if l1 is None or l2 is None:
        return None
    if l1.tail != l2.tail:
        return None
    longest = l1.head if l1.length > l2.length else l2.head
    shortest = l1.head if l1.length < l2.length else l2.head
    start_node_in_longest = get_kth_node(longest, abs(l1.length - l2.length))
    while start_node_in_longest != shortest:
        start_node_in_longest = start_node_in_longest.next
        shortest = shortest.next

    return shortest


def get_kth_node(longest, no_of_nodes_to_skip):
    current = longest
    while no_of_nodes_to_skip and current:
        current = current.next
        no_of_nodes_to_skip -= 1

    return current

if __name__ == '__main__':
    node_common = SingleLinkedList.Node(7)
    l1 = SingleLinkedList()
    l1.append(3)
    l1.append(1)
    l1.append(5)
    l1.append(9)
    l1.append_node(node_common)
    l2 = SingleLinkedList()
    l2.append(4)
    l2.append(6)
    l2.append_node(node_common)
    node_common.next = SingleLinkedList.Node(2)
    node_common.next.next = SingleLinkedList.Node(1)

    print(get_intersecting_node(l1, l2))
