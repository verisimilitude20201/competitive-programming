"""
Complexity:
-----------
Solution 1
----------
TimeL: O(N^2)
Space: O(1)

Solution 2
----------
TimeL: O(N^2)
Space: O(N)/O(1)

Solution 3
----------
TimeL: O(N log N)
Space: O(1)
"""
class Solution1:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stone_1 = self.remove_largest(stones)
            stone_2 = self.remove_largest(stones)
            if stone_1 != stone_2:
                stones.append(stone_1 - stone_2)
        return stones[0] if stones else 0
    
    def remove_largest(self, stones):
         largest_num_at_index = stones.index(max(stones))
         stones[largest_num_at_index], stones[-1] = stones[-1], stones[largest_num_at_index]

         return stones.pop()

class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 != stone_2:
                bisect.insort(stones, stone_1 - stone_2)

        return stones[0] if stones else 0

class Solution3:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        return -stones[0] if stones else 0
        