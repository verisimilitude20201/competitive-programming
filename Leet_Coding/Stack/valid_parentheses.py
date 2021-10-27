class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lefty = "({["
        righty = ")}]"
        for char in s:
            if char in lefty:
               stack.append(char)
            elif char in righty:
               if len(stack) == 0:
                   return False
               if righty.index(char) != lefty.index(stack.pop()):
                   return False

        return len(stack) == 0