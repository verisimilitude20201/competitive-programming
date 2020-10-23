"""
Conceptual - 3 Pointers approach
--------------------------------
1.  prev, next = NULL, head = current = self.nodes

		head
NULL	1	->	2	->	3	->	4	-> NULL
prev    current
next

2. next = current.next

		head
NULL	1	->	2	->	3	->	4	-> NULL
prev    current next


3. current.next = prev

		head
NULL <-	1		2	->	3	->	4	-> NULL
prev    current next

4. prev = current

		head
NULL <-	1		2	->	3	->	4	-> NULL
        prev    next
        current

5. current = next

		head
NULL <-	1		2	->	3	->	4	-> NULL
        prev    next
                current

6. next = current.next

		head
NULL <-	1		2	->	3	->	4	-> NULL
        prev   current next 

7. current.next = prev

		head
NULL <-	1	<-	2		3	->	4	-> NULL
        prev   current next

8. current = prev

		head
NULL <-	1	<-	2		3	->	4	-> NULL
                current next
                prev

9. current = next

		head
NULL <-	1	<-	2		3	->	4	-> NULL
                prev   next
                       current

10. current = next

		head
NULL <-	1	<-	2		3	->	4	-> NULL
                prev    current next

11. current.next = prev

		head
NULL <-	1	<-	2	<-	3		4	-> NULL
                prev    current next


12. prev = current

		head
NULL <-	1	<-	2	<-	3		4	-> NULL
                       current next
                       prev

13. current = next

		head
NULL <-	1	<-	2	<-	3		4	-> NULL
                        prev  next
                              current

14. next = current.next

		head
NULL <-	1	<-	2	<-	3		4	-> NULL
                        prev   current  next

15. current.next = prev

		head
NULL <-	1	<-	2	<-	3	<-	4	-> NULL
                        prev   current  next

16. prev = current

		head
NULL <-	1	<-	2	<-	3	<-	4	-> NULL
                              current  next
                              prev

17. current = next
NULL <-	1	<-	2	<-	3	<-	4	-> NULL
                               prev      next
                                         current

18. current is NULL so break out of the loop 

19. head = prev

NULL <-	1	<-	2	<-	3	<-	4	
                                head

Complexity
-----------
O(N) Time
O(1) Space


"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        
        return head