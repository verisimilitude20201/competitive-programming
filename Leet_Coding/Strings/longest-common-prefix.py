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
----------
Time O(N): We loop  through N-strings in array
Space O(N): We are creating successive substrings of the prefix till its found in given string. Since Python's strings are immutable, every time a new substring is created
a new character array is allocated to it. Worst case is O(N)

Solution 2:
----------

Input:

["leets", "leetc", "leetcode", "leeds"]

Output

"lee"

1.  l    e     e      t     s

    low  = 0
    high = 5
    middle = 2

   Consider prefix "le"

   "le" startswith "leets" --> True
   "le" startswith "leetcode" --> True
   "le" startswith "leetc" --> True
   "le" startswith "leeds" --> True

   "le" is common prefix in all strings.

2.  Increment low by middle + 1
    low = 3
    high = 5
    middle = 4

    Consider prefix "lee"

      "lee" startswith "leets" --> True
      "lee" startswith "leetcode" --> True
      "lee" startswith "leetc" --> True
      "lee" startswith "leeds" --> True

     "lee" is common prefix in all strings.

3. Increment low by middle + 1

    low = 5
    high = 5
    middle = 5

    Consider prefix "leet"

    "leet" startswith "leets" --> True
    "leet" startswith "leetcode" --> True
    "leet" startswith "leetc" --> True
    "leet" startswith "leeds" --> False

    "leet" is not common prefix in all strings


4. Increment high by middle - 1
    low = 5
    high = 4
    middle = 4

    But here, low <= high condition is False so we break out of the while loop.

    Therefore, the longest common prefix is "lee" viz.

Complexity
---------

Time O(N * log(m)): N is the length of strings in the list and m is the length of the minimum string from that list
Space O(log(m)):  m is the length of the minimum string from that list. Strings are immutable in Python..

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
    
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        min_length = sys.maxsize
        for string in strs:
            min_length = min(min_length, len(string))
        low = 0
        high = min_length

        while low <= high:
            middle = int((low + high) / 2)
            if self.is_common_prefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1

        return strs[0][0 : int((low + high) / 2)]

    def is_common_prefix(self, strs: List[str], length: int) -> bool:
        prefix = strs[0]
        prefix = prefix[0: length]
        for i in range(1, len(strs)):
            string = strs[i]
            if not string.startswith(prefix):
                return False

        return True