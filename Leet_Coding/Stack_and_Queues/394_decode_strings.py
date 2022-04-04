"""
decodeString1
------------
Time Complexity: O(max_k ^ count_k * N)
Space Complexity: O(SUM(max_k ^ count_k * N))

Example: if the string is 20[a10[bc]]
max_k = 20 i.e. the number of times the string is to be repeated
count_k = 2 i.e. there are two nestings
N = number of encoded strings

"""
class Solution:
    def decodeString1(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                decoded_string = []
                while len(stack) and stack[-1] != "[":
                    decoded_string.append(stack.pop())
                stack.pop()
                k = 0
                base = 1
                while len(stack) and str.isdigit(stack[-1]):
                    k += int(stack.pop()) * base
                    base *= 10
                while k > 0:
                    for i in range(len(decoded_string) - 1, -1, -1):
                        stack.append(decoded_string[i])
                    k -= 1
        output = [None] * len(stack)
        for i in range(len(stack) - 1, -1, -1):
            output[i] = stack.pop()
        
        return "".join(output)