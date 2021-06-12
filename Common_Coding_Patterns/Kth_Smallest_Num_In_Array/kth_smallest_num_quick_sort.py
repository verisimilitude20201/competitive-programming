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
Time: Worst case is O(N^2) which happens when the partitioning happens between arrays of size 1 and N - 1. Best/Average case is O(N log N) because
we just select one of the halves of the array. 

Space: O(1)

"""
def find_Kth_smallest_number(nums, k):
  return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
  p = partition(nums, start, end)

  if p == k - 1:
    return nums[p]

  if p > k - 1:  # search lower part
    return find_Kth_smallest_number_rec(nums, k, start, p - 1)

  # search higher part
  return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
  if low == high:
    return low

  pivot = nums[high]
  for i in range(low, high):
    # all elements less than 'pivot' will be before the index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  # put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()