"""
Problem
-------
Given the head of a LinkedList with a cycle, find the length of the cycle.

Approach
-------
Fast and slow pointers. Fast moves by two positions, slow by one position
1. If there is not a cycle, Fast finishes looping through the list.
2. If there is a cycle, fast jumps back from the cycle to an earlier node followed by slow 
and eventually they point to the same node.
3. If there is a cycle, initialize another pointer to the meeting point of fast and slow. Increment
the cycle count till this pointer equals pointer slow.

Complexity:
----------
Time: O(n) -> n number of nodes in the list.
Space: O(1)


"""

class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next


def find_cycle_length(head):
    slow, fast = head, head
    has_cycle = False
    cycle_current_node = None
    while fast is not None and fast._next is not None:
        fast = fast._next._next
        slow = slow._next
        if fast == slow:
            return calculate_cycle_length(slow)

    return 0


def calculate_cycle_length(slow):
    cycle_length = 0
    cycle_current_node = slow
    while True:
        cycle_length += 1
        cycle_current_node = cycle_current_node._next
        if cycle_current_node == slow:
            break
    return cycle_length


def main():
    head = Node(1)
    head._next = Node(2)
    head._next._next = Node(3)
    head._next._next._next = Node(4)
    head._next._next._next._next = Node(5)
    head._next._next._next._next._next = Node(6)
    head._next._next._next._next._next._next = head._next._next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head._next._next._next._next._next._next = head._next._next._next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()

