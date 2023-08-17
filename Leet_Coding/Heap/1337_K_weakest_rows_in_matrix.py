"""
Complexity:
----------
Solution 1:
----------
Time: O(M log M + N M)
Space: O(M)

Solution 2:
----------
Time: O(M log M + N M)
Space: O(M)

Solution 3:
----------
Time: O(M log M + N M)
Space: O(M)
"""
class Solution1:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengths = []
        for i in range(len(mat)):
            strengths.append((sum(mat[i]), i))
        strengths.sort()
        weakest = []
        for i in range(k):
            weakest.append(strengths[i][1])
        return weakest
    

class Solution2:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengths = collections.defaultdict(list)
        for i in range(len(mat)):
            strength = sum(mat[i])
            strengths[strength].append(i)

        sorted_strengths = sorted(strengths.keys())
        weakest = []
        for strength in sorted_strengths:
            for index in strengths[strength]:
                weakest.append(index)
                if len(weakest) >= k:
                    break
            if len(weakest) >= k:
                    break

        return weakest

class Solution3:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengths = collections.defaultdict(list)
        for i in range(len(mat)):
            strength = self.get_strength(mat[i])
            strengths[strength].append(i)
        sorted_strengths = sorted(strengths.keys())
        weakest = []
        for strength in sorted_strengths:
            for index in strengths[strength]:
                weakest.append(index)
                if len(weakest) >= k:
                    break
            if len(weakest) >= k:
                    break

        return weakest

    def get_strength(self, row):
        left = 0
        right = len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] == 1:
                left = mid + 1
            else:
                right = mid
        return left