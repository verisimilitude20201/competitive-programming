"""
Problem:
-------
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

Example:
-------
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None,  k = 3
     head

     3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 -> None
     -----------
                    ----------
                                   -----

Approach
-------
0)   
  None     	 		1 		-> 2 -> 3 -> 4 -> 5 -> None
  previous  		head
  last_node_pp      current
                    last_node_sl



1) 

None       <-		1 	<-  2 <-  3   			4 			-> 5 -> None
                                  previous  	current
  last_node_pp                                  next
                    last_node_sl


2) None	 			3 		-> 2  ->  1     			4 -> 5 -> None
   last_node_pp     head              last_node_sl      current
                    previous                			next


3) previous = last_node_sl

   None	 			3 		-> 2  ->  1     			4 		-> 5 -> None
   last_node_pp     head              last_node_sl      current
                                      previous          next

4) last_node_sl = current

    None 			3 		-> 2  ->  1     			4 		-> 5 -> None
   last_node_pp     head                                current
                                      previous          next
                                                        last_node_sl

5) last_node_pp = previous

 			3 		-> 2  ->  1     			4 		-> 5 -> None
           head               last_node_pp     current
                              previous         next
                                               last_node_sl

Complexity:
---------
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


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    previous = None
    current = head

    while True:
        last_node_of_previous_list = previous
        last_node_of_sub_list = current
        i = 0
        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        if last_node_of_previous_list is not None:
            last_node_of_previous_list.next = previous
        else:
            head = previous

        last_node_of_sub_list.next = current
        if current is None:
            break
        previous = last_node_of_sub_list

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
