"""
Problem:
-------
Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

Example:
-------
Input: [
  [1,0,1],
  [1,1,1],
  [0,1,1]
]
Output: [
  [0,1,0],
  [0,0,0],
  [0,0,1]
]

First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]

Approach:
--------
To reverse just swap the ith element to  (len(arr) - i - 1)th element
To invert, just XOR each element with 1.

Complexity:
----------
Time: O(N^2)
Space: O(1)

"""

def flip_and_invert_image(matrix):
    for i in range(len(matrix)):
        matrix1 = matrix[i]
        for j in range((len(matrix1) // 2) + 1):
            index_to_be_replaced = len(matrix1) - j - 1
            matrix1[j], matrix1[index_to_be_replaced] = matrix1[index_to_be_replaced] ^ 1, matrix1[j] ^ 1

    return matrix


def main():
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
