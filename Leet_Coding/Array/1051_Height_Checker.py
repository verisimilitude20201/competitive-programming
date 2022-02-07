"""
Explanation:
-----------

heightChecker1
--------------
1. Simply created an expected array by creating a copy of heights array and sorting it.
2. Used two-pointers on the two arrays to compare them

Complexity:
----------

heightChecker1
--------------
Time: O(N log N)
Space: O(N)

"""
class Solution:
    def heightChecker1(self, heights: List[int]) -> int:
        i = 0
        j = 0
        expected = heights.copy()
        expected.sort()
        mismatch_cnt = 0
        while i < len(heights) and j < len(expected):
            if heights[i] != expected[j]:
                mismatch_cnt += 1

            i += 1
            j += 1

        return mismatch_cnt