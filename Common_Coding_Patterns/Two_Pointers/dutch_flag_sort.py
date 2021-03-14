"""
Problem
-------
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; 
and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem

Example:
-------
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]

0) [2, 2, 0, 1, 2, 0]
    L              H   
    i 

1) [0, 2, 0, 1, 2, 2]
    L           H   
    i

2) [0, 2, 0, 1, 2, 2]
       L        H   
       i

   [0, 2, 0, 1, 2, 2]
       L     H   
       i

   [0, 1, 0, 2, 2, 2]
       L  H   
       i

3) [0, 1, 0, 2, 2, 2]
       L  H   
          i

4) [0, 1, 0, 2, 2, 2]
       L  H   
          i

   [0, 0, 1, 2, 2, 2]
       L  H   
          i

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
Two Pointers: Move all 0s before low pointer and all 2s after high pointer. Low and high point to 0th and (n - 1)st element


Complexity
---------
    Time: O(N)
    Space: O(1) because it's in-place
"""


def dutch_flag_sort(arr):
  i = 0
  low = 0
  high = len(arr) - 1
  while i <= high:
    if arr[i] == 0:
      arr[low], arr[i] = arr[i], arr[low]
      i += 1
      low += 1
    elif arr[i] == 1:
      i += 1
    else:
      arr[high], arr[i] = arr[i], arr[high]
      high -= 1


def main():
  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)

main()
