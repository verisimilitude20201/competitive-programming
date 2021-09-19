"""
Explanation:
----------
1. Use two stacks - stack 2 will hold the elements in sorted order.
2. Keep on popping from stack 2 into stack 1 till the correct place of the element is found. 

Complexity:
----------
1. Time: O(N^2)
2. Space: O(N)

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


def sort_stack(stack1: Stack):
    stack2 = Stack()
    while not stack1.is_empty():
        element = stack1.pop()
        while not stack2.is_empty() and element < stack2.peek():
            stack1.push(stack2.pop())
        stack2.push(element)

    while not stack2.is_empty():
        stack1.push(stack2.pop())


def main():
    stack = Stack()
    stack.push(12)
    stack.push(8)
    stack.push(3)
    stack.push(5)
    stack.push(7)
    stack.push(1)
    sort_stack(stack)


main()
