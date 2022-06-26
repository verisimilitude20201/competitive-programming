"""
Complexity:
----------
Time: O(1) for all and O(K) for addToIndex and deleteToIndex
Space: O(1), we just maintain a reference to the sentinal node.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.head
        for _ in range(-1, index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        prev = self.head
        current = self.head.next
        for _ in range(index):
            prev = current
            current = current.next
        node = ListNode(val)
        prev.next = node
        node.next = current
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        prev = self.head
        current = self.head.next
        for _ in range(index):
            prev = current
            current = current.next
        prev.next = current.next
        current.next = None
        self.length -= 1