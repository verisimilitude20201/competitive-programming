"""
Explanation:
-----------
1. Use Set.
2. Consider -ve numbers also
3. If a single occurence of 0 is there, it will be False. If [0, 0] it will be True. This is an edge
case.
4. If you add all array elements in Set first and then check, it may not work because edge case 3 
may fail

Complexity:
---------
Time: O(N)
Space: O(N)
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if (num % 2 == 0 and num / 2 in seen) or (num * 2 in seen):
                return True
            seen.add(num)
        return False