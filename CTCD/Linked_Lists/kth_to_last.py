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
    index = kth_to_last1(head.next, k) + 1
    if index == k:
        print("Kth to last node is " + str(head.data))
    return index



class Counter:
    def __init__(self):
        self.index = 0

def kth_to_last2(head, k, counter):
    if head is None:
        return None
    node = kth_to_last2(head.next, k, counter)
    counter.index += 1
    if counter.index == k:
        return head
    return node


def kth_to_last3_iterative(head, k):
    p1 = head
    p2 = head
    for i in range(k):
        if p1 is None:
            return None
        p1 = p1.next
    while p1:
        p1 = p1.next
        p2 = p2.next

if __name__ == '__main__':
    slist = SingleLinkedList()
    slist.append(1)
    slist.append(2)
    slist.append(3)
    slist.append(2)
    slist.append(5)

    kth_to_last1(slist.head, 2)
    counter = Counter()

    kth_to_last2(slist.head, 2, counter)