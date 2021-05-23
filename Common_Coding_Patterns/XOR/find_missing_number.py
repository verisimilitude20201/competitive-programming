"""
Problem:
-------
Given an array of integers from 1 to N, find one missing number

Example:
-------
[1, 5, 2, 6, 4]

Approach:
--------
1. Compute XOR of numbers from 1 to N
2. Compute the XOR of arr[0] to arr[N - 1]
3. Compute the XOR of 1 and 2 to find the missing number.

1      0001  
2      0010
3      0011
4      0100
5      0101


x1 = 1 XOR 2 = 0011
x1 = 0011 XOR 3 = 0000
x1 = 0000 XOR 0100(4)  = 0100
x1 = 0100 XOR 0101(5) = 0001

x2 = 0001
x2 = 0001 (1) XOR 0101(5) = 0100
x2 = 0100 XOR 0100 (2) = 0000
x2 = 0000 XOR 0110(6) = 0110
x2 = 0110 XOR 0100(4) = 0010


x1 ^ x2 = 0110 = 3

Complexity:
---------
Time: O(1)
Space: O(1)

"""

def find_missing_number(arr):
    n = len(arr) + 1
    x1 = 1
    for i in range(2, n + 1):
        x1 ^= i

    x2 = arr[0]
    for j in range(1, n - 1):
        x2 ^= arr[j]

    return x1 ^ x2


def main():
    arr = [1, 5, 2, 6, 4]
    print('Missing number is:' + str(find_missing_number(arr)))


main()
