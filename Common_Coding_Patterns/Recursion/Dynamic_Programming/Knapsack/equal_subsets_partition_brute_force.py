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
Time: O(2^N)
Space: O(N)

"""
def can_partition(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False

    return can_partition_recursive(nums, s // 2, 0)


def can_partition_recursive(nums, s, current_index):
    if s == 0:
        return True

    n = len(nums)

    if n == 0 or current_index >= n:
        return False

    if nums[current_index] <= s:
        if can_partition_recursive(nums, s - nums[current_index], current_index + 1):
            return True

    return can_partition_recursive(nums, s, current_index + 1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
