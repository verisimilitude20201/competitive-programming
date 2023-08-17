"""
Complexity:
----------
Solution 1:
----------
Time: O(N + k)
Space: O(N + k)
"""
class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_number = -math.inf
        m_cache = {}
        points = defaultdict(int)
        for num in nums:
            points[num] += num
            max_number = max(num, max_number)

        def max_points(number):
            if number == 0:
                return 0
            if number == 1:
                return points[1]
            
            if number in m_cache:
                return m_cache[number]
            m_cache[number] = max(max_points(number - 1), max_points(number - 2) + points[number])
            
            return m_cache[number]


        return max_points(max_number)