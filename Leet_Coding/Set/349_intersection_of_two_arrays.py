"""
Complexity:
-----------
Solution1
------------
Time: O(M + N)
Space: O(d) Where d is the number of distinct elements in the smaller list.


Solution2
---------
Time: O(M + N)
Space: O(M + N)

Solution3
---------
Time: O(M + N) can be O(M * N) when the load factor is quite high
Space: O(M + N)

"""

from typing import List


class Solution1:
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            self.intersection(nums2, nums1)

        num_set = set()
        for num in nums1:
            num_set.add(num)

        i = 0
        for num in nums2:
            if num in num_set:
                nums1[i] = num
                i += 1
                num_set.remove(num)

        return nums1[:i]

class Solution2:
    def get_intersection(self, set1: set[int], set2: set[int]) -> List[int]:
        return [x for x in set1 if x in set2]
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
          set1 = set(nums1)
          set2 = set(nums2)
          
          if len(nums1) > len(nums2):
              return self.get_intersection(set2, set1)
          else:
              return self.get_intersection(set1, set2)

class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
          set1 = set(nums1)
          set2 = set(nums2)
          
          return list(set1 & set2)