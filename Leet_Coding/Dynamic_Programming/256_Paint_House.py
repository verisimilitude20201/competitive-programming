"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
from functools import lru_cache
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @lru_cache(max_size=None)
        def paint_cost(i, color):
            total_cost = costs[i][color]
            if i == len(costs) - 1:
                pass

            elif color == 0:
                total_cost += min(paint_cost(i + 1, 1), paint_cost(i + 1, 2))
            elif color == 1:
                total_cost += min(paint_cost(i + 1, 0), paint_cost(i + 1, 2))

            elif color == 2:
                total_cost += min(paint_cost(i + 1, 0), paint_cost(i + 1, 1))

            return total_cost

        if len(costs) == 0:
            return 0

        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))