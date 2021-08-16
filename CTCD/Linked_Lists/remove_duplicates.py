"""
Complexity:
----------
remove_duplicates1
  Time: O(N)
  Space: O(N)

remove_duplicates2
    Time: O(N)
    Space: O(N)

"""

from base.base_linked_list import SingleLinkedList


def remove_duplicates1(slist):
    visited_node_values = set()
    if slist is None:
        return None
    n_prev = slist.head
    if n_prev.next is None:
        return slist

    n_next = n_prev.next
    while n_next is not None:
        if n_next.data in visited_node_values:
            n_prev.next = n_next.next
        else:
            visited_node_values.add(n_prev.data)
            n_prev = n_prev.next
        n_next = n_next.next

    slist.print_list()

def remove_duplicates2(slist):
    current = slist.head
    runner = current
    while current is not None:
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next

if __name__ == '__main__':
    slist = SingleLinkedList()
    slist.append(1)
    slist.append(2)
    slist.append(3)
    slist.append(2)
    slist.append(5)

    remove_duplicates1(slist)
