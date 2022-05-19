"""
Complexity:
----------
Solution 1
----------
Time: O(N * CS * S)

Where N = Length of list
CS = length of the common prefix of two strings
S = average length of each string for taking the slice

Space: O(S)
"""

class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[0: len(prefix) - 1]
                if prefix == "":
                    return ""

        return prefix