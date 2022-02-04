"""
Explanation:
-----------
Two pointers Success Case
 0  1  2  3  4  5  6  7
[0, 2, 3, 4, 5, 2, 1, 0]
             i  
             j

Get the limits of the left and right bounds right. 
- Left pointer goes only upto the 3rd last index
- Right pointer goes only upto the 3rd index from first (i.e. index 2)


Complexity:
---------
Time: O(N)
Space: O(1)
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left = 0
        right = len(arr) - 1
        while left < len(arr) - 2 and arr[left] < arr[left + 1]:
            left += 1
        while right > 1 and arr[right] < arr[right - 1]:
            right += 1
        
        return left == right