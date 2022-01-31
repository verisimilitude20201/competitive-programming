"""
Complexity:
----------
duplicateZeros1
---------------
    Time: O(N^2)
    Space: O(1)

duplicateZeros2
---------------
    Time: O(N)
    Space: O(N)

duplicateZeros3
---------------
    Time: O(N)
    Space: O(1)
    
"""
class Solution:
    def duplicateZeros1(self, arr: List[int]) -> None:
        k = len(arr) - 1
        for i in range(len(arr) - 1, -1, 0):
            if arr[i - 1] == 0:
                while k > i:
                    arr[k] = arr[k - 1]
                    k -= 1
                arr[i] = 0
            k = len(arr) - 1
    
    def duplicateZeros2(self, arr: List[int]) -> None:
        result = [None] * len(arr)
        d = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                result[d] = 0
                d += 1
                result[d] = 0
            else:
                result[d] = arr[i]
            d += 1


        return result
    
    def duplicateZeros3(self, arr: List[int]) -> None:
        length = len(arr) - 1
        left = 0
        no_of_zeroes = 0
        for left in range(len(arr)):
            if left > length - no_of_zeroes:
                break
            
            if arr[left] == 0:
                if left == length - no_of_zeroes:
                    arr[left] = 0
                    break
                no_of_zeroes += 1
        
        last_element = length - no_of_zeroes
        for j in range(last_element, -1, -1):
            if arr[j] == 0:
                arr[j + no_of_zeroes] = 0
                no_of_zeroes -= 1
                arr[j + no_of_zeroes] = 0
            else:
                arr[j + no_of_zeroes] = arr[j]