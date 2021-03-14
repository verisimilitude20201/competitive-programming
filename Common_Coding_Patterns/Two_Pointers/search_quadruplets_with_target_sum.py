"""
Problem
-------
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example:
-------
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.


Approach
-------
Two Pointers (Reduce 4 sum problem to 2 sum one)

a + b + c + d = target

c + d = target - (a + b)

0) Input: [2, 0, -1, 1, -2, 2], target=2
           

1) Input: [-2, -1, 0, 1, 2, 2], target=4
            i      j  L     H  

   Input: [-2, -1, 0, 1, 2, 2], target=4
            i      j     L  H  
         
         [-2, 0, 2, 2]

2) Input: [-2, -1, 0, 1, 2, 2], target=4
            i         j  L  H  


3) Input: [-2, -1, 0, 1, 2, 2], target=3
                i  j  L     H 

              [-1, 0, 1, 2]

Complexity
---------
    Time: O(N^3 + N log N) ~  O(N^3)
            N log N for sorting the array. 
    Space: O(N)
"""

def search_quadruplets_with_target_sum(arr, target):
    arr.sort()
    high = len(arr) - 1
    quadruplets = []
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr) - 1:
            low = j + 1
            while low < high:
                current_sum = arr[low] + arr[high]
                target_sum = target - (arr[i] + arr[j])
                if current_sum == target_sum:
                    quadruplets.append([arr[i], arr[j], arr[low], arr[high]])
                    low += 1
                    high -= 1
                elif current_sum > target_sum:
                    high -= 1
                else:
                    low += 1
            j += 1

    return quadruplets


def main():
    print(search_quadruplets_with_target_sum([2, 0, -1, 1, -2, 2], 2))

main()
