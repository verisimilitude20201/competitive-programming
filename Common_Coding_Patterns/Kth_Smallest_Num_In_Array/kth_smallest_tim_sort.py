"""
Problem:
-------
Given an unsorted array of numbers, find Kth smallest number in it.

Example:
-------
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Complexity:
---------
Time: O(N * Log N)
Space: O(1)

"""

def find_kth_smallest_num_in_array(nums, k):
    return sorted(nums)[k - 1]


def main():
    print("Kth smallest number is: " +
          str(find_kth_smallest_num_in_array([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_kth_smallest_num_in_array([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_kth_smallest_num_in_array([5, 12, 11, -1, 12], 3)))


main()