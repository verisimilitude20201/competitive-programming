"""
Problem
-------
Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number

Example:
-------
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.


  0)  [2, 5, 3, 10],  target = 30, product = 1,  left = 0, right = 0, temp_list = [], result = []
       L
       R

  1) [2, 5, 3, 10],  target = 30, product = 1,  left = 0, right = 0, temp_list = [[2]], result = [[3]]
      L
      R

  2) [2, 5, 3, 10],  target = 30, product = 10,  left = 0, right = 1, temp_list = [[5]], result = [[2], [5]]
      L
         R

     [2, 5, 3, 10],  target = 30, product = 10,  left = 0, right = 1, temp_list = [[5], [5, 2]], result = [[2], [5], [5, 2]]
      L
         R

  3) [2, 5, 3, 10],  target = 30, product = 30,  left = 0, right = 2, temp_list = [], result = [[2], [5], [5, 2]]
      L
            R

     [2, 5, 3, 10],  target = 30, product = 15,  left = 1, right = 2, temp_list = [[3]], result = [[2], [5], [5, 2], [3]]
         L
            R 

     [2, 5, 3, 10],  target = 30, product = 15,  left = 1, right = 2, temp_list = [[3, 5]], result = [[2], [5], [5, 2], [3], [3, 5]]
         L
            R

  4) [2, 5, 3, 10],  target = 30, product = 150,  left = 1, right = 2, temp_list = [], result = [[2], [5], [5, 2], [3], [3, 5]]
         L
                R

  5) [2, 5, 3, 10],  target = 30, product = 30,  left = 1, right = 2, temp_list = [], result = [[2], [5], [5, 2], [3], [3, 5]]
            L
                R 

  6) [2, 5, 3, 10],  target = 30, product = 10,  left = 1, right = 2, temp_list = [], result = [[2], [5], [5, 2], [3], [3, 5]]
                L
                R

     [2, 5, 3, 10],  target = 30, product = 10,  left = 1, right = 2, temp_list = [], result = [[2], [5], [5, 2], [3], [3, 5], [10]]
                L
                R     


Approach
-------
Two Pointers along with Sliding Window

Sliding window is required because we need to keep on increasing the window till the product >= target, following which we reduce the window one by one.


Complexity
---------
    Time: O(N^2)
    Space: O(N^2)
"""


def find_all_subarrays_less_than_product(arr, target):
  subarrays = []
  left = 0
  product = 1
  for right in range(len(arr)):
    product *= arr[right]
    while product >= target and left < len(arr):
      product /= arr[left]
      left += 1

    collect_subarrays = []
    for j in range(right, left - 1, -1):
      collect_subarrays.append(arr[j])
      subarrays.append(list(collect_subarrays))

  return subarrays


def main():
  print(find_all_subarrays_less_than_product([2, 5, 3, 10], 30))
  print(find_all_subarrays_less_than_product([8, 2, 6, 5], 50))

main()
