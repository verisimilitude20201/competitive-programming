"""
Complexity:
----------
dailyTemperatures
-----------------
Time: O(N^2)
Space: O(N)

dailyTemperatures1
------------------
Time: O(N) Since every element could be added to Stack only once.
Space: O(N)


dailyTemperatures3
------------------
Time: O(N) --> No two indexes are visited twice.
Space: O(1)

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
    
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answers = [0] * n
        stack = []
        for current_day, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prev_day = stack.pop()
                answers[prev_day] = current_day - prev_day
            stack.append(current_day)
        
        return answers
    
    def dailyTemperatures3(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answers = [0] * n
        for current_day in range(n - 1, -1, -1):
            if hottest <= temperatures[current_day]:
                hottest = temperatures[current_day]
                continue
            future_day = 1
            while temperatures[future_day + current_day] <= temperatures[current_day]:
                future_day += answers[future_day + current_day]
            answers[current_day] = future_day

        return answers


solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))