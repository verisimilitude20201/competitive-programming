"""
Problem
-------
Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

Example:
-------
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 2
head

Output

2 -> 1  -> 3 -> 4  -> 6 -> 5 -> 7 -> 8
------               -------

Approach:
--------
Similar to reversing every k elements of a list. The only difference is we would need to skip k nodes and continue the process after one iteration

0) 
	1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 2
	head

	Output

	2 -> 1  -> 3 -> 4  -> 6 -> 5 -> 7 -> 8
    ------               -------
1) 

None				1 		-> 	2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 2
previous			head
last_node_of_pp     current
	                last_node_of_sl


2) 

None	<-			1 		<- 	2    ->  3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 2
			        head                 next
last_node_of_pp                previous  current
	                last_node_of_sl

3)

None	<-			2 		-> 	1    ->  3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 2
			        head                 next
last_node_of_pp     previous             current
	                            
	                            last_node_of_sl

4) 

None	<-			2 		-> 	1    ->  3 -> 4 -> 5 -> 6 -> 7 -> 8, k = 2
			        head                 next
last_node_of_pp                 previous current
	                            
	                            last_node_of_sl


5) 

2 		-> 	1    ->  			3 		-> 	4 -> 5 -> 6 -> 7 -> 8
head                 			next
            previous 			current

            last_node_of_pp     last_node_of_sl


6) Skip K-elements

2 		-> 	1    ->  			3 		-> 	4 -> 5 -> 6 -> 7 -> 8, j = 0
head                 			next
            previous 			current

            last_node_of_pp     last_node_of_sl



2 		-> 	1    ->  			3 		-> 	4 -> 5 -> 6 -> 7 -> 8, j = 1
head                 			next
                                previous   current

            last_node_of_pp     last_node_of_sl


2 		-> 	1    ->  			3 		-> 	4 -> 5 -> 6 -> 7 -> 8, j = 1
head                 			next
                                previous   current

            last_node_of_pp     last_node_of_sl




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


def reverse_alternating_k_element_sub_list(head, k):
    if k <= 1 or head is None:
        return head

    current = head
    previous = None
    while True:
        last_node_of_previous_part = previous
        last_node_of_sub_list = current
        i = 0
        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
        if last_node_of_previous_part is None:
            head = previous
        else:
            last_node_of_previous_part.next = previous
        if last_node_of_sub_list is not None:
            last_node_of_sub_list.next = current
        previous = last_node_of_sub_list

        j = 0
        while current is not None and j < k:
            current = current.next
            previous = previous.next
            j += 1
        if current is None:
            break
            
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
    result = reverse_alternating_k_element_sub_list(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
