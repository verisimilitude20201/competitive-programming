"""
Problem
-------
Given the head of a LinkedList with a cycle, find the starting node of the cycle.

Approach
-------
Fast and slow pointers. 
1. Once you find the cycle length, set two pointers - pointer1 and pointer2 
2. Shift pointer2 by 1 and pointer2 by cycle_length + 1. Their meeting point is the starting node. 

Complexity:
----------
Time: O(n) -> n number of nodes in the list.
Space: O(1)


"""

class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next


def find_cycle_start_node(head):
    cycle_length = find_cycle_length(head)
    if cycle_length == 0:
        return None
    pointer1, pointer2 = head, head
    while True:
        pointer_2_counter = cycle_length + 1
        while pointer_2_counter > 0:
            pointer2 = pointer2._next
            pointer_2_counter -= 1
        pointer1 = pointer1._next
        if pointer1 == pointer2:
            break

    return pointer1._value


def find_cycle_length(head):
    fast, slow = head, head
    while fast is not None and fast._next._next is not None:
        fast = fast._next._next
        slow = slow._next
        if fast == slow:
            return calculate_cycle_length(slow)
    return 0


def calculate_cycle_length(slow):
    cycle_node = slow
    cycle_length = 0
    while True:
        cycle_length += 1
        cycle_node = cycle_node._next
        if cycle_node == slow:
            break

    return cycle_length


def main():
    head = Node(1)
    head._next = Node(2)
    head._next._next = Node(3)
    head._next._next._next = Node(4)
    head._next._next._next._next = Node(5)
    head._next._next._next._next._next = Node(6)
    head._next._next._next._next = head._next
    print("Cycle Start Node" + str(find_cycle_start_node(head)))


main()

