"""
Explanation:
-----------
Case 1) Between min_val and max_val
    
    3  -> 4 -> 1 -> 3,    2
    H          P    C 

Case 2)  

 i)  Greater than max_val; prev.val > insertVal
     3 -> 5 -> 7 -> 9 -> 1,   10 
     H              P    C
                
 
 ii) Less then min_val; current.val >= insertVal
      3 -> 5 -> 7 -> 9 -> 1 -> 3,   0 
      H              P    C


Case 3) Single Node

 1 -> 1, 0 

Case 4) Empty List

None, 5

5 -> 5

Complexity:
----------
Time: O(N)
Space: O(1)

"""
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        prev, current = head, head.next
        to_insert = False
        while True:
            if prev.val <= insertVal <= current.val:
                to_insert = True
            elif prev.val > current.val:
                if prev.val <= insertVal or current.val >= insertVal:
                    to_insert = True
            if to_insert:
                prev.next = node
                node.next = current
                return head
            prev = current
            current = current.next
            if prev == head:
                break
        prev.next = node
        node.next = current
        return head