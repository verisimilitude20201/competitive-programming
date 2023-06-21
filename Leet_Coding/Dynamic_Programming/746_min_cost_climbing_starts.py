class Solution1:
    # Top Down
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def dp(i):
            if i <= 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2]
            
            return memo[i]
        
        return dp(len(cost))


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # 1. An array that stores the answers
        dp = [0] * (n + 1)
        
        # 3. Base cases are implicitly defined as they are 0

        for i in range(2, n + 1):
            # 2. Recurrence relation
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]