class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and self.are_two_chars_equal_with_opp_case(stack[-1], s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        
        if len(stack):
            return "".join(stack)
        return ""
    
    def are_two_chars_equal_with_opp_case(self, c1: str, c2: str) -> bool:
        c1_index_in_alphabet = self.get_char_index_in_alphabet(c1)
        
        c2_index_in_alphabet = self.get_char_index_in_alphabet(c2)
        
        if c1 != c2:
            if c1.lower() == c2.lower() and c1_index_in_alphabet == c2_index_in_alphabet:
                return True
        
        return False
    
    def get_char_index_in_alphabet(self, c: str) -> int:
        return ord(c) - ord("a") if c.islower() else ord(c) - ord("A")