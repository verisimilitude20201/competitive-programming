"""
Solution 1
----------
1. Consider the longest prefix as the 0th element of the string array
2. From first string onwards, 
2.1 Compare this prefix with string to see if it is actually the prefix.
2.2 If Yes, go to second string.
2.3 If No, take substring(0, len(prefix) - 1) and compare again
3. When loop ends, and prefix is found in all strings, return.

Complexity:
Time O(N): We loop  through N-strings in array
Space O(N): We are creating successive substrings of the prefix till its found in given string. Since Python's strings are immutable, every time a new substring is created
a new character array is allocated to it. Worst case is O(N)


"""
class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            string = strs[i]
            while string.startswith(prefix) == False:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""         

        return prefix