"""
Matching element using a stack

Time complexity O(m) -- N is the number of tags of the input source
Space complexity O(m) -- m is the number of HTML tags in the string.
"""
class Stack:
    def __init__(self):
        self._data = []

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0


class MatchingHtml:

    def __init__(self, raw_html):
        self._raw_html = raw_html

    def is_html_valid(self):
        stack = Stack()
        opening_angle_bracket = self._raw_html.find("<")
        while opening_angle_bracket != -1:
            closing_angle_bracket = self._raw_html.find(">", opening_angle_bracket + 1)
            if closing_angle_bracket == -1:
                return False
            tag_name = self._raw_html[opening_angle_bracket + 1 : closing_angle_bracket]
            if not tag_name.startswith("/"):
                stack.push(tag_name)
            else:
                if stack.is_empty():
                    return False

                if tag_name[1:] != stack.pop():
                    return False

            opening_angle_bracket = self._raw_html.find("<", closing_angle_bracket + 1)
        return stack.is_empty()


raw_html = "Abhijit <strong>Ghatnekar</strong><i> is my name"
matching_html =  MatchingHtml(raw_html)
print(matching_html.is_html_valid())

