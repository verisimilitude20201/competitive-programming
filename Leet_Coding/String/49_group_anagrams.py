"""
Complexity:
----------

Solution1
---------
Time: O(N * K Log K) K is the maximum length of each string, N is the length of strs
Space: O(N * K)


Solution2
--------
Time: O(N * K)
Space: O(N * K)

"""
from collections import defaultdict

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_groups = defaultdict(list)
        for s in strs:
            ana_groups[tuple(sorted(s))].append(s)
        return list(ana_groups.values())

from collections import defaultdict

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ana_groups[tuple(count)].append(s)
        return ana_groups.values()