"""
Explanation:
-----------
1. We go to the last node of each linked list using recursion and maintain the current partial sum, carry and resulting list as the stack unwinds
2. If one of the lists is larger than the other, we simply pad them (prepend them with 0s) from the left.


Complexity:
----------
Time: O(N)
Space: O(N)
"""
from base.base_linked_list import SingleLinkedList


class PartialSum:
    def __init__(self):
        self._carry = 0
        self._result = SingleLinkedList()
        self._total = 0

    def set_carry(self, carry):
        self._carry = carry

    def set_result(self, result):
        self._result = result

    def set_total(self, total):
        self._total = total

    def get_carry(self):
        return self._carry

    def get_result(self):
        return self._result

    def get_total(self):
        return self._total


def sum_of_linked_list_forward(node1, node2) -> PartialSum:
    if node1 is None and node2 is None:
        return PartialSum()

    partial_sum = sum_of_linked_list_forward(node1.next, node2.next)
    total = node1.data + node2.data + partial_sum.get_carry()
    carry = 1 if total >= 10 else 0
    partial_sum.set_carry(carry)
    result = partial_sum.get_result()
    result.prepend(total % 10)
    partial_sum.set_total(total)
    partial_sum.set_result(result)

    return partial_sum


if __name__ == '__main__':
    l1 = SingleLinkedList()
    l1.append(6)
    l1.append(1)
    l1.append(7)

    l2 = SingleLinkedList()
    l2.append(2)
    l2.append(9)
    l2.append(5)

    partial_sum = sum_of_linked_list_forward(l1.head, l2.head)
    partial_sum.get_result().print_list()
