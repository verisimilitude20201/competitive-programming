"""
Complexity:
----------
Time: O(N^2)
Space: O(N)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        for day in range(len(temperatures)):
            for future_day in range(day + 1, len(temperatures)):
                if temperatures[day] < temperatures[future_day]:
                    answers[day] = future_day - day
                    break

        return answers


solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))