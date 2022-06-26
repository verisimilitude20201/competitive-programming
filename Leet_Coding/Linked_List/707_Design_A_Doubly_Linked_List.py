class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(-1)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head.next
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        node = ListNode(val)
        prev_ptr = self.head
        current = self.head.next
        for _ in range(index):
            prev_ptr = current
            current = current.next
        prev_ptr.next = node
        node.next = current
        node.prev = prev_ptr
        if current:
            current.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev_ptr = self.head
        current = self.head.next
        for _ in range(index):
            prev_ptr = current
            current = current.next
        prev_ptr.next = current.next
        if current.next:
            current.next.prev = current
        self.size -= 1