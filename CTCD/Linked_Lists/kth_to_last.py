"""
Complexity:
----------
Time: O(N)
Space: O(N)

"""
from base import SingleLinkedList


def kth_to_last1(head, k):
    if head is None:
        return 0
    index = kth_to_last(head.next, k) + 1
    if index == k:
        print("Kth to last node is " + str(head.data))
    return index


if __name__ == '__main__':
    slist = SingleLinkedList()
    slist.append(1)
    slist.append(2)
    slist.append(3)
    slist.append(2)
    slist.append(5)

    kth_to_last1(slist.head, 2)