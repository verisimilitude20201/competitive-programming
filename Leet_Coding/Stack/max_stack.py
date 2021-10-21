"""
Time: O(N)
Space: O(N)
"""

class MaxStack:

    def __init__(self):
        self.__data = []

    def push(self, x: int) -> None:
        if len(self.__data) == 0:
            self.__data.append((x, x))
        else:
            top_element = self.peekMax()
            max_x = None if top_element is None else max(top_element, x)
            self.__data.append((x, max_x))

    def pop(self) -> int:
        if len(self.__data) == 0:
            return None
        top_element = self.__data.pop()
        return top_element[0]

    def top(self) -> int:
        if len(self.__data) == 0:
            return None
        return self.__data[-1][0]

    def peekMax(self) -> int:
        if len(self.__data) == 0:
            return None
        return self.__data[-1][1]

    def popMax(self) -> int:
        m = self.peekMax()
        top = self.top()
        d = []
        while m != top:
            d.append(self.pop())
            top = self.top()
        self.pop()
        reversed(d)
        while d:
            self.push(d.pop())
        return m