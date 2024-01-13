"""
Complexity:
---------
Time: O(N)
Space: O(N)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def decodings(index):
            if index == len(s):
                return 1

            if s[index] == "0":
                return 0
            
            if index == len(s) - 1:
                return 1

            answer = decodings(index + 1)
            if int(s[index: index + 2]) <= 26:
                answer += decodings(index + 2)

            return answer

        return decodings(0)