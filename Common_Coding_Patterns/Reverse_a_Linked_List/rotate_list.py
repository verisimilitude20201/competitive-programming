"""
Problem
-------
Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.


Example:
-------
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None, k = 2
    head


    Output
    5 -> 6 -> 1 -> 2 -> 3 -> 4

Approach
--------
0) 
	1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None, k = 2
    head


    Output
    5 -> 6 -> 1 -> 2 -> 3 -> 4

1) Calculate length and last_node

i)
	1 			-> 2 -> 3 -> 4 -> 5 -> 6 -> None, list_length = 1
	head
	last_node

ii) 

1 			-> 2 -> 3 -> 4 -> 5 -> 6 -> None, list_length = 6
head
                                   last_node


2) Connect last_node to head

1  -> 2 -> 3 -> 4 -> 5 -> 6 -> 1
head                     last_node


3) Compute effective skip_length

rotations %= list_length 
2 % 6 = 2

skip_length = 6 - 2 = 4

4) Skip by 4


i) 

1 			-> 2 -> 3 -> 4 -> 5 -> 6 -> 1
head
last_node_of_skip_list             last_node


ii) 

1 			-> 2 -> 3 -> 4 							-> 5 ->  6 -> 1
head
                         last_node_of_skip_list             last_node


iii) 

1 			-> 2 -> 3 -> 4 							-> 5 ->  6 -> 1
                                                       head
                         last_node_of_skip_list             last_node



5)

5 -> 6 -> 1 -> 2 -> 3 -> 4 -> 5 
head                     last_node_of_skip_list 

6) 

5 -> 6 -> 1 -> 2 -> 3 -> 4 -> None
head                     last_node_of_skip_list

Complexity:
----------
Time: O(N)
Space: O(1)
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


def rotate(head, rotations):
    if rotations <= 1 or head is None or head.next is None:
        return head

    list_length = 1
    last_node = head
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1

    last_node.next = head
    rotations = rotations % list_length
    skip_length = list_length - rotations
    i = 0
    last_node_of_kth_sub_list = head
    while i < skip_length:
        last_node_of_kth_sub_list = last_node_of_kth_sub_list.next
        i += 1

    head = last_node_of_kth_sub_list.next
    last_node_of_kth_sub_list.next = None

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
