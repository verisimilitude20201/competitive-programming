"""
Problem
-------
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. 
The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example:
--------
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true

Approach
-------
Fast and slow pointers. 
1. Find the middle of the Linkedlist by slow and fast pointers
2. From the middle, reverse the second end of the list

               None
               ^
               | 
     2 -> 4 -> 6 <- 4 <- 2 

     So here the middle of the list points to None and second half of the list has their pointers reversed

3. Compare each element in each half.

Complexity:
----------
Time: O(n) -> n number of nodes in the list.
Space: O(1)


"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_linked_list_palindrome(head):
    if head is None or head.next is None:
        return True
    slow, fast = get_middle_of_list(head)
    second_head_at_end = reverse(slow)
    copy_of_second_head = second_head_at_end
    while head is not None and second_head_at_end is not None:
        if head.value != second_head_at_end.value:
            break
        head = head.next
        second_head_at_end = second_head_at_end.next
    reverse(copy_of_second_head)
    if head is None or second_head_at_end is None:
        return True
    return False


def get_middle_of_list(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow, fast


def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_linked_list_palindrome(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_linked_list_palindrome(head)))


main()
