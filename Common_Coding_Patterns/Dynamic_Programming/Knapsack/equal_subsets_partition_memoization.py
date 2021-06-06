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
    s = sum(nums)
    if s % 2 != 0:
        return False
    dp = [[-1 for x in range((s // 2) + 1)] for y in range(len(nums))]

    return True if can_partition_recursive(nums, s // 2, 0, dp) == 1 else False


def can_partition_recursive(nums, s, current_index, dp):
    if sum == 0:
        return 1

    n = len(nums)

    if n == 0 or current_index >= n:
        return False

    if dp[current_index][s] == -1:
        if nums[current_index] <= s:
            if can_partition_recursive(nums, s - nums[current_index], current_index + 1, dp):
                dp[current_index][s] = 1
                return 1

            dp[current_index][s] = can_partition_recursive(nums, s, current_index + 1, dp)

    return dp[current_index][s]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
