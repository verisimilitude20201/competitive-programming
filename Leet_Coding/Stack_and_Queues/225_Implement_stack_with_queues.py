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