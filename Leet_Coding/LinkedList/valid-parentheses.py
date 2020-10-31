"""
Approach
-------
1. Keep pushing all left parentheses, brackets and braces on Stack
2. If any right parenthesis, brace or bracket is encountered, pop off the last element of the Stack.
3. 

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