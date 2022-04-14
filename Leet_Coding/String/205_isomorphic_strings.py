"""
Complexity:
---------

Solution1
---------
Time: O(N)
Space: O(1) it's ASCII character set.

"""

class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for c1, c2 in zip(s, t):
            if c1 not in s_to_t and c2 not in t_to_s:
                s_to_t[c1] = c2
                t_to_s[c2] = c1
            elif s_to_t.get(c1) != c2 or t_to_s.get(c2) != c1:
                return False

        return True
    
class Solution2:
    def transform(self, s: string) -> str:
        index_map = {}
        new_str = []
        for i, char in enumerate(s):
            if char not in index_map:
                index_map[char] = str(i)
            new_str.append(index_map[char])
        
        return ":".join(new_str)
        
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transform(s) == self.transform(t)