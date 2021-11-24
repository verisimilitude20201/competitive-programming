"""
Problem:
-------
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.

Example:
-------
2 -> 4 -> 6 -> 8 -> 10 -> None

None <- 2 <- 4 <- 6  <- 8 <- 10 


Complexity
---------
reverse1:
    Time: O(N)
    Space: O(1)

reverse2:
    Time: O(N)
    Space: O(N)

"""

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse1(head):
    prev_ptr = None
    current = head
    while current is not None:
        next_ptr = current.next
        current.next = prev_ptr
        prev_ptr = current
        current = next_ptr

    return prev_ptr

def reverse2(head):
    if head is None or head.next is None:
        return head
    p = reverse(head.next)
    head.next.next = head
    head.next = None

    return p

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
