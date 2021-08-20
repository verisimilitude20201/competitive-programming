"""
Explanation
-----------

sum_of_linked_list_reverse
-------------------------

7 -> 1 -> 6
5 -> 9 -> 2

It's actually the sum of 617 and 295

sum_of_linked_list_forward
--------------------------
6 -> 1 -> 7
2 -> 9 -> 5


Complexity:
----------
Time: O(min(M, N)) Where M and N are lengths of list1 and list2
Space: O(1)
"""


from base.base_linked_list import SingleLinkedList


def sum_of_linked_list_reverse(node1, node2):
    result = SingleLinkedList()
    carry = 0
    while node1 is not None or node2 is not None:
        x = 0 if node1 is None else node1.data
        y = 0 if node2 is None else node2.data
        total = carry + x + y
        node = SingleLinkedList()
        node.data = total % 10
        if result.head is None:
            result.head = node
        else:
            node.next = result.head
            result.head = node
        carry = 1 if total >= 10 else 0
        if node1 is not None:
            node1 = node1.next
        if node2 is not None:
            node2 = node2.next
    return result


if __name__ == '__main__':
    l1 = SingleLinkedList()
    l1.append(7)
    l1.append(1)
    l1.append(6)

    l2 = SingleLinkedList()
    l2.append(5)
    l2.append(9)
    l2.append(2)
    result = SingleLinkedList()

    result1 = sum_of_linked_list_reverse(l1.head, l2.head)
    result1.print_list()
