"""
Problem
------
Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are 
inserted alternately to the nodes from the first half in reverse order. 
So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

Example
-------
Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 

Approach
--------
Fast & Slow pointers
    1. Find middle of linked list 
    2. Reverse second half of it.
    3. Loop through both halves in same loop with pointer manipulations


Complexity
---------
Time: O(N)
Space: O(1)

"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    middle_node = get_middle_node_of_linked_list(head)
    first_head = head
    second_head = reverse_second_half_of_list(middle_node)
    while first_head is not None and second_head is not None:
        first_head_next = first_head.next
        second_head_next = second_head.next
        first_head.next = second_head
        second_head.next = first_head_next
        first_head = first_head_next
        second_head = second_head_next

        # set the next of the last node to 'None'
    if first_head_next is not None:
        first_head_next.next = None


def get_middle_node_of_linked_list(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    middle_node = slow

    return middle_node


def reverse_second_half_of_list(middle_node):
    prev = None
    while middle_node is not None:
        next = middle_node.next
        middle_node.next = prev
        prev = middle_node
        middle_node = next

    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
