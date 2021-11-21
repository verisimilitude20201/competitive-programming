"""
Explanation:
-----------
Time: O(numRows^2)
Space: O(numRows^2)


"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            res = [0] * (i + 1)
            res[0] = 1
            res[-1] = 1

            for j in range(1, len(res) - 1):
                res[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(res)

        return result