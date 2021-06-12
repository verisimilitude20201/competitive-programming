"""
Problem:
------
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example:
-------
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

Complexity:
----------
Time: O(N * S) Where N is total number of numbers and S is the sum of all numbers
Space: O(N * S)

"""

def can_partition(nums):
    S = sum(nums)
    if S % 2 != 0:
        return False

    s = S // 2
    n = len(nums)

    dp = [[False for i in range(s + 1)] for j in range(n) ]

    for i in range(0, n):
        dp[i][0] = True

    for j in range(1, s+1):
        dp[0][j] = nums[0] == j

    for i in range(1, n):
        for j in range(1, s + 1):
            if dp[i-1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    return dp[n - 1][s]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
