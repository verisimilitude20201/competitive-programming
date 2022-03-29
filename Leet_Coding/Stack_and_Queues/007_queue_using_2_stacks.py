"""
Complexity:
----------
MyQueue1
--------
For each element other than newly inserted one, we push and pop two times so 4 and for newly inseted one 2 times.
    Time: O(4n + 2) ~ O(N)
    Space: O(N)
"""

class MyQueue1:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = -1

    def push(self, x: int) -> None:
        if len(self.s1) == 0:
            self.front = x

        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        self.s1.pop()
        if not len(self.s1) == 0:
            self.front = self.s1[0]

    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        return len(self.s1) == 0

class MyQueue2:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = -1

    def push(self, x: int) -> None:
        """
        Time: O(1)
        Space: O(N)
        """
        if len(self.s1) == 0:
            self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        """
        Time: O(1) Amortized
        Space: O(N)
        """
        if len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())

        x = self.s2.pop()
        if len(self.s1) == 0 and len(self.s2) > 0:
            self.front = self.s2[-1]
            
        return x

    def peek(self) -> int:
        """
        Time/Space: O(1)
        """
        return self.front

    def empty(self) -> bool:
        """
        Time/Space: O(1)
        """
        
        return len(self.s1) == 0 and len(self.s2) == 0

        

