"""
Complexity:
---------
Solution1:
---------
Time: O(N^2)
Space: O(N^2)

Solution2
---------
Time: O(N^(k/2))
Space: O(N^(k/2))

Where N is the length of each lists and k is the number of arrays
"""
import collections
from typing import List


class Solution1:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        total_map = collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                total_map[a + b] += 1
        for c in nums3:
            for d in nums4:
                cnt += total_map[-(c + d)]
        return cnt

class Solution2:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        lists = [nums1, nums2, nums3, nums4]
        m = collections.defaultdict(int)
        
        def n_sum_count():
            get_hash(0, 0)
            return count_complements(len(lists) // 2, 0)
        
        def get_hash(i, total):
            if i == (len(lists) // 2):
                m[total] += 1
            else:
                for a in lists[i]:
                    get_hash(i + 1, total + a)
        
        def count_complements(i, complement):
            if i == len(lists):
                return m[complement]
            cnt = 0
            for b in lists[i]:
                cnt += count_complements(i + 1, complement - b)
            return cnt
            
        
        return n_sum_count()

solution = Solution()
print(solution.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))

