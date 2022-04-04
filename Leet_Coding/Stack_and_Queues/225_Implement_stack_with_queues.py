"""
Complexity:
----------

MyStack1
-------
Push O(1), Pop O(N)

MyStack2
-------
Push O(N), Pop O(1)

MyStack3
-------
Push O(N), Pop O(1)

"""

from collections import deque

class MyStack1:

    def __init__(self):
        self.Q1 = deque([])
        self.Q2 = deque([])
        self.front = None
        
    def push(self, x: int) -> None:
        self.Q1.append(x)
        self.front = x
        

    def pop(self) -> int:
        if self.empty():
            return None
        while len(self.Q1) > 1:
            self.Q2.append(self.Q1.popleft())
        x = self.Q1.popleft()
        self.Q1, self.Q2 = self.Q2, self.Q1
        if len(self.Q1) > 0:
            self.front = self.Q1[-1]
        return x
        

    def top(self) -> int:
        if self.empty():
            return True
        return self.front
        

    def empty(self) -> bool:
        return len(self.Q1) == 0 and len(self.Q2) == 0

class MyStack2:

    def __init__(self):
        self.Q1 = deque([])
        self.Q2 = deque([])
        self.front = None

    def push(self, x: int) -> None:
        self.front = x
        self.Q2.append(x)
        if len(self.Q1) > 0:
            while len(self.Q1) > 0:
                self.Q2.append(self.Q1.popleft())

        self.Q1, self.Q2 = self.Q2, self.Q1

    def pop(self) -> int:
        x = self.Q1.popleft()
        self.front = self.Q1[0] if len(self.Q1) > 0 else None
        return x

    def top(self) -> int:
        if self.empty():
            return None
        return self.front

    def empty(self) -> bool:
        return len(self.Q1) == 0 and len(self.Q2) == 0

class MyStack3:

    def __init__(self):
        self.Q = deque([])
        self.front = None

    def push(self, x: int) -> None:
        self.Q.append(x)
        self.front = x
        size = len(self.Q)
        while size > 1:
            self.Q.append(self.Q.popleft())
            size -= 1

    def pop(self) -> int:
        if self.empty():
            return None
        x = self.Q.popleft()
        self.front = self.Q[0] if len(self.Q) else None
        return x

    def top(self) -> int:
        if self.empty():
            return None
        return self.front

    def empty(self) -> bool:
        return len(self.Q) == 0