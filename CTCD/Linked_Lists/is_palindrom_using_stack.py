"""
Explanation:
-----------
1. We store the first half of the list on a Stack using fast/slow pointer method
2. To account for the odd number of nodes in list, we increment the pointer.
3. We pop the elemenets from stack and compare them with the second half of the list

Complexity:
----------
Time: O(N)
Space: O(N / 2) (We store first half list on Stack)

"""
from base.base_linked_list import SingleLinkedList
from base.stack import Stack


def is_palindrome(head):
    fast = head
    slow = head
    stack = Stack()
    while fast.next is not None and fast.next is not None:
        stack.push(slow.data)
        fast = fast.next.next
        slow = slow.next
    if fast is not None:
        slow = slow.next

    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next

    return True


if __name__ == '__main__':
    l1 = SingleLinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(1)

    print(is_palindrome(l1.head))
