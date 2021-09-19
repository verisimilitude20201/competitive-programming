"""
Explanation:
-----------
1. For queue, peek and pop() are simply reversed to return oldest elements (peek() and dequeue() for a queue) rather than newest ones.
2. Just use another auxillary stack for holding them..

Complexity:
----------
1. Time: O(N) N is the length of the stack(s). 
2. Space: O(N) Since we require one auxillary stack.
"""
class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self._data[-1]

    def is_empty(self):
        return len(self) == 0


class MyQueue:

    def __init__(self):
        self.stack_newest = Stack()
        self.stack_oldest = Stack()

    def enqueue(self, element):
        """

        :rtype: object
        """
        self.stack_newest.push(element)

    def shift_stacks(self):
        while not self.stack_newest.is_empty():
            self.stack_oldest.push(self.stack_newest.pop())

    def dequeue(self):
        self.shift_stacks()
        return self.stack_oldest.pop()

    def peek(self):
        self.shift_stacks()
        return self.stack_oldest.peek()


def main():
    my_queue = MyQueue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    my_queue.enqueue(6)
    print(my_queue.dequeue())

main()