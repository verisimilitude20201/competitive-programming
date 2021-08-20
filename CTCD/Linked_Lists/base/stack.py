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
