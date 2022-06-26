"""
Complexity:
----------
Solution 1 & 2:
--------------
Time: O(N)
Space: O(N)

"""
class Solution1:
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        front_pointer = head
        def traverse_recursively(current_node):
            nonlocal front_pointer
            if current_node is None:
                return True
            
            if not traverse_recursively(current_node.next):
                return False
            
            if current_node.val != front_pointer.val:
                return False
            front_pointer = front_pointer.next
            return True
        
        return traverse_recursively(head)


class Solution:
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        if length == 1:
            return True
        mid = length // 2
        

        current = head
        stack = []
        for _ in range(mid):
            stack.append(current.val)
            current = current.next

        if length % 2 != 0:
            current = current.next
        while current:
            if stack.pop() != current.val:
                return False
            current = current.next

        return True