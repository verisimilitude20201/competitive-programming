"""
Problem
-------
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

Approach
-------
Fast and slow pointers. Fast moves by two positions, slow by one position
1. If there is not a cycle, Fast finishes looping through the list.
2. If there is a cycle, fast jumps back from the cycle to an earlier node followed by slow 
and eventually they point to the same node.

Complexity:
----------
Time: O(n) -> n number of nodes in the list.
Space: O(1)


"""

class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next


def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast._next is not None:
        fast = fast._next._next
        slow = slow._next
        if fast == slow:
            return True
    return False


def main():
    head = Node(1)
    head._next = Node(2)
    head._next._next = Node(3)
    head._next._next._next = Node(4)
    head._next._next._next._next = Node(5)
    head._next._next._next._next._next = Node(6)

    print("Has Cycle " + str(has_cycle(head)))
    head._next._next._next._next = head._next
    print("Has Cycle " + str(has_cycle(head)))

main()
