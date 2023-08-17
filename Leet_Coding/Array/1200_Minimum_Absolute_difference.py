"""
Complexity:
----------
Time: O(n log n)
Space: O(log n) / O(n)
"""
class Solution1:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = math.inf
        for i in range(len(arr) - 1):
          min_diff = min(min_diff, abs(arr[i + 1] - arr[i]))

        result = []  
        for i in range(len(arr) - 1):
          diff = abs(arr[i + 1] - arr[i])
          if diff == min_diff:
            result.append([arr[i], arr[i + 1]])

        return result

class Solution2:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = math.inf
        answer = []
        for i in range(len(arr) - 1):
          current_diff = abs(arr[i + 1] - arr[i])
          if current_diff == min_diff:
            answer.append([arr[i], arr[i + 1]])
          elif current_diff < min_diff:
            answer = [[arr[i], arr[i + 1]]]
            min_diff = current_diff

        return answer