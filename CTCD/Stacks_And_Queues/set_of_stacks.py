class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self._is_empty():
            raise Exception("Stack is empty!")
        return self._data.pop()

    def peek(self):
        if self._is_empty():
            raise Exception("Stack is empty!")
        return self._data[-1]

    def _is_empty(self):
        return len(self._data) == 0

class SetOfStacks:
    MAX_STACK_SIZE = 2

    def __init__(self):
        self.stacks = []

    def push(self, element):
        stack = self.get_last_stack()
        if stack is not None and len(stack) < SetOfStacks.MAX_STACK_SIZE:
            stack.push(element)
        else:
            stack = Stack()
            stack.push(element)
            self.stacks.append(stack)

    def pop(self):
        stack = self.get_last_stack()
        element = stack.pop()
        if len(stack) == 0:
            del self.stacks[len(self.stacks) - 1]

        return element

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[len(self.stacks) - 1]


def main():
    set_of_stacks = SetOfStacks()
    set_of_stacks.push(1)
    set_of_stacks.push(2)
    set_of_stacks.push(3)
    set_of_stacks.push(4)
    set_of_stacks.push(5)
    set_of_stacks.push(6)
    print(set_of_stacks.pop())

main()