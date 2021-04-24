"""
Problem
-------

Example:
-------
1 -> 2 -> 3 -> 4 -> 5 -> None, p = 2, q = 4
     head

     Output

     1 -> 4 -> 3 -> 2 -> 5 -> None
     head

0)   1 -> 2 -> 3 -> 4 -> 5 -> None, p = 2, q = 4
     head

     Output

     1 -> 4 -> 3 -> 2 -> 5 -> None
     head

1) Find p and node_before_p

   i) None  1 -> 2 -> 3 -> 4 -> 5 -> None, p = 2, q = 4,   prev = None, current = head, i = 0, i < p - 1 = True

            head
      prev current

  ii) None  1 -> 2 -> 3 -> 4 -> 5 -> None, p = 2, q = 4,   prev = None, current = head, i = 1, i < p - 1 = 1 < 2 - 1 = False

            head
            prev current


  iii) node_before_p = prev, node_p = current


2) Reverse list between p = 2 and q = 4

    i) None -> 2  ->  3 -> 4  -> 5 -> None,  i = 0, next = current.next, i < q - p + 1 = True
       prev current  next

    ii) None <- 2    -> 3   -> 4 -> 5 -> None,  i = 0, i < q - p + 1 = True
        prev   current  next


    iii) None <- 2     3   -> 4 -> 5 -> None,  i = 0, i < q - p + 1 = True
               current   next
               prev

    iv) None <- 2       3   -> 4 -> 5 -> None,  i = 0, i < q - p + 1 = True
                       next
               prev    current

    v) None <- 2       3   ->   4     -> 5 -> None,  i = 1, i < q - p + 1 = True
                               next
               prev    current  

    vi)  None <- 2  <-  3     4     -> 5 -> None,  i = 1, i < q - p + 1 = True
                                 next
               prev    current

    vii) None <- 2  <-  3      4     -> 5 -> None,  i = 1, i < q - p + 1 = True
                       prev    next
                       current
    
    viii) None <- 2  <-  3      4     -> 5 -> None,  i = 1, i < q - p + 1 = True
                       prev    next
                               current

    ix) None <- 2  <-  3      4     -> 5   -> None,  i = 2, i < q - p + 1 = True
                       prev            next
                              current

    x) None <- 2  <-  3    <-      4        5   -> None,  i = 2, i < q - p + 1 = True
                      prev                 next
                                 current

    xi) None <- 2  <-  3    <-      4        5   -> None,  i = 2, i < q - p + 1 = True
                                    prev    next
                                 current

    xii) None <- 2  <-  3    <-      4        5   -> None,  i = 3, i < q - p + 1 = False

                                     prev    next
                                            current

3) Connect the 3 parts of the list - list before p, list between p and q and list after q

   i) 1 -> None,  None <- 2  <-  3    <-  4   5            -> None
    node_before_p,                            node_after_q 


  ii) node_before_p.next  = node_q

      1 -> 4 -> 3 -> 2 -> None,   5 -> None

  iii) node_p.next = node_after_q 

      1 -> 4 -> 3 -> 2 -> 5 -> None


Approach:
--------
Reverse a list

1. Find the pth node
2. Reverse the list between the pth and qth node
3. Keep track of node before pth node and node after qth node
4. Connect the node_before_p.next with q_node
5. Connect node_p.next = node_after_q

Tricky Part:
-----------
1. While reversing a list between p and q, the condition should be current.next is Not None. If this is'nt the case, both current and next will point to the last
node of the list.

2. While reversing a list maintain a prev pointer to None. current.next = prev gives rise to a self-loop if current == prev.

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


def reverse_sub_list(head, p, q):
    if p == q:
        return head

    prev_ptr = None
    current = head
    i = 0
    while i < p - 1:
        prev_ptr = current
        current = current.next
        i += 1

    node_before_p = prev_ptr
    node_p = current

    i = 0
    prev_ptr = None
    while current.next is not None and i < q - p + 1:
        next_ptr = current.next
        current.next = prev_ptr
        prev_ptr = current
        current = next_ptr
        i + 1

    node_q = prev_ptr
    node_after_q = current

    if node_before_p is not None:
        node_before_p.next = node_q
    else:
        head.next = node_q

    node_p.next = node_after_q

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
