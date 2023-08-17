"""
Complexity:
----------
Time: O(MIN(K, N) + N log MIN(K, N)))
Space: O(MIN(K, N))
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        num_rows = len(matrix)
        for i in range(min(num_rows, k)):
            min_heap.append((matrix[i][0], i, 0))
        
        heapq.heapify(min_heap)
        value = 0
        while k:
            value, row, column = heapq.heappop(min_heap)
            if column < num_rows - 1:
                heapq.heappush(min_heap, (matrix[row][column + 1], row, column + 1))
            k -= 1
        
        return value