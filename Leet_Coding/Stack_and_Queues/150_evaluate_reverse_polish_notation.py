"""
Complexity:
-----------
evalRPN1
--------
Time: O(n^2): Every operator removal causes the left-shift of tokens
after the operator by 1 due to pop() behavior
Space: O(1)

evalRPN2:
---------
Time: O(N)
Space: O(N)

"""
class Solution:
    def evalRPN1(self, tokens: List[str]) -> int:
        current_position = 0
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        while len(tokens) > 1:
            while tokens[current_position] not in "*/+-":
                current_position += 1
            operator = operations[tokens[current_position]]
            number_1 =  int(tokens[current_position - 2])
            number_2 =  int(tokens[current_position - 1])
            tokens[current_position] = operator(number_1, number_2)
            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1
        return tokens[0]
    
    def evalRPN2(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                number_2 = stack.pop()
                number_1 = stack.pop()
                operator = operations[token]
                result = operator(number_1, number_2)
                stack.append(result)
        return stack.pop()