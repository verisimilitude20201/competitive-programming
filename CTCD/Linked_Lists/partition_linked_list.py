"""
Explanation:
-----------
0)

3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
h
t
n

1) 

next = 5

3 -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
h
t
          n 
		  
		  
2)

next = 8

3 -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
h
t
          n 
		  
3 ->  5 -> 8 -> 5 -> 10 -> 2 -> 1
h
      t 
           n 

3) next = 5

3 -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
     h
                t   n 
           
 
5 -> 8 -> 5 -> 10 -> 2 -> 1
     t 
          n 
		  
4) next = 10

3 -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
     h
                    t    n 

5 -> 8 -> 5 -> 10 -> 2 -> 1
          t 
               n 

5) next = 2

3 -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
     h
                          t    n 


5 -> 8 -> 5 -> 10 -> 2 -> 1
               t 
                     n 
6) next = 1

3 -> 2 -> 3 -> 5 -> 8 -> 5 -> 10 ->   -> 1
     h
     n                        t     


5 -> 8 -> 5 -> 10 ->  -> 1
               t 
                     
			  
7) next = None

3 -> 1-> 2 -> 3 -> 5 -> 8 -> 5 -> 10 -> None  
     h                            tail
     n

Complexity:
----------
Time: O(N)
Space: O(1)

"""

from base import SingleLinkedList

def partition_linked_list(node, partition):
    head = node
    tail = node
    while node is not None:
        next = node.next
        if int(node.data) < partition:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None

    return head

if __name__ == '__main__':
    slist = SingleLinkedList()
    slist.append("3")
    slist.append("5")
    slist.append("8")
    slist.append("5")
    slist.append("10")
    slist.append("2")
    slist.append("1")

    partition_linked_list(slist.head, 5)