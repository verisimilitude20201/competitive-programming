"""
Approach
-------
1. Keep pushing all left parentheses, brackets and braces on Stack
2. If any right parenthesis, brace or bracket is encountered, pop off the last element of the Stack.
3. Check if it matches. If not return False.
4. Return if the stack is empty. If yes, the parenthesis are balanced.

Complexity
---------

Space: O(N) - We allocate N characters on Stack at max.
Time: O(N) - We loop through N characters in string.

"""
class Stack:
    class  Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first is None

    def push(self, data):
        if self.first is None:
            self.first = self.Node(data)
        else:
            old_first = self.first
            self.first = self.Node(data)
            self.first.next = old_first

    def pop(self):
        data = None
        if not self.is_empty():
            data = self.first.data
            self.first = self.first.next

        return data

class Solution:

    matching_pairs = {
    "}": "{",
    "]": "[",
    ")": "("
    }


    def __init__(self):
        self.stack = Stack()

    def isValid(self, s: str) -> bool:
        for char in s:
            if self.is_opening_bracket(char):
                self.stack.push(char)

            elif self.is_closing_bracket(char):
                if not self.is_bracket_matched(char):
                    return False
        
        return self.stack.is_empty()

    def is_opening_bracket(self, s):
        return s == "{" or s == "[" or s == "("


    def is_closing_bracket(self, s):
        return s == "}" or s == "]" or s == ")"

    def is_bracket_matched(self, bracket):
        bracket_to_be_matched = self.matching_pairs[bracket]
        if not self.stack.is_empty() and bracket_to_be_matched == self.stack.pop():
            return True
        return False


"""
One more solution
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


class MatchingParenthesis:
    left_brackets = "[{("
    right_brackets = "]})"

    def __init__(self, brackets):
        self._brackets = brackets

    def is_opening_bracket(self, c):
        return c in self.left_brackets

    def do_bracket_pairs_match(self):
        stack = Stack()
        for c in self._brackets:
            if self.is_opening_bracket(c):
                stack.push(c)
            else:
                if stack.is_empty():
                    return False
                if self.left_brackets.index(stack.pop()) != self.right_brackets.index(c):
                    return False

        return stack.is_empty()


if __name__ == '__main__':
    matching_parenthesis = MatchingParenthesis("{[()]}")
    print(matching_parenthesis.do_bracket_pairs_match())

    matching_parenthesis = MatchingParenthesis("{[())))))){}]}")
    print(matching_parenthesis.do_bracket_pairs_match())
