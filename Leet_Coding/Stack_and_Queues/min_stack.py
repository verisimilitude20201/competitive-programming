"""
Explanation:
-----------
To have O(1) access to the minimum element, always keep it at the top of the stack.


Complexity:
----------
Time: O(1)
Space: O(1)

"""
class MinStack:
    class __Element:
        def __init__(self, data, min_element):
            self.data = data
            self.min_element = min_element

    def __init__(self):
        self.__data = []
        self.current_min = None

    def push(self, val: int) -> None:
        if len(self.__data) == 0:
            element = self.__Element(val, val)
        else:
            top_element = self.__get_top_element()
            element = self.__Element(val, min(val, top_element.min_element))

        self.__data.append(element)

    def pop(self) -> None:
        if len(self.__data) == 0:
            return None
        element = self.__data.pop()

        return element.data

    def top(self) -> int:
        top_element = self.__get_top_element()
        return None if top_element is None else top_element.data

    def getMin(self) -> int:
        top_element = self.__get_top_element()
        return None if top_element is None else top_element.min_element

    def __get_top_element(self):
        if len(self.__data) == 0:
            return None
        element = self.__data[-1]

        return element