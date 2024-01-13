"""
Complexity:
----------
Time: O(S * N * K)
Space: O(N)
"""
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                word_len = len(word)
                if i >= word_len - 1 and (i == word_len - 1 or dp[i - word_len]):
                    if s[i - word_len + 1: i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]
    

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dp(i):
            if i < 0:
                return True

            for word in wordDict:
                if i >= len(word) - 1 and dp(i - len(word)):
                    if s[i - len(word) + 1: i + 1] == word:
                        return True

            return False

        return dp(len(s) - 1)