"""
Approach
---------

Example:  

Input: array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Output: [3, 9]

1. Find the maximum and minimum out of order numbers.

Let S denote 'sorted' and NS denote 'not sorted'

 0  1  2  3  4   5   6  7   8  9  10  11  12
[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
 S  S  S  S  S   NS  NS NS  NS S  S    S   S 


2. Sub-array [5, 8] is not sorted. The minimum unsorted number is 6, maximum is 12.

3. From left, compare minimum unsorted number to each element of array until its greater. So 6 goes at position 3.

4. From right, compare maximum unsorted number to each element until its smaller. So 12 goes at position 9.

Complexity
---------
1. Space O(1): We are not storing any extra information apart from maximum and minimum unsorted element.
2. Time O(N): We loop through the entire array

"""



def subarraySort(array):
    minUnsortedNumber = float("inf")
    maxUnsortedNumber = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minUnsortedNumber = min(minUnsortedNumber, num)
            maxUnsortedNumber = max(maxUnsortedNumber, num)


    if minUnsortedNumber == float("inf"):
        return [-1, -1]

    subArrayLeftIdx = 0
    while minUnsortedNumber >= array[subArrayLeftIdx]:
        subArrayLeftIdx += 1
    subArrayRightIdx = len(array) - 1
    while maxUnsortedNumber <= array[subArrayRightIdx]:
        subArrayRightIdx -= 1
    return [subArrayLeftIdx, subArrayRightIdx]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]
