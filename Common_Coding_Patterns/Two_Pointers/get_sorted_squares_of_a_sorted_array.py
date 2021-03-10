"""
Problem
-------
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example:
-------
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]


Approach
-------
Two Pointers

1. Similar to finding the target sum in a sorted array. The placement of left and right pointers is similar.


Complexity
---------
    Time: O(N) 
    Space: O(1)

def get_sorted_squares_of_a_sorted_array(arr):
    if len(arr) == 0:
        return []
    squares = [0] * len(arr)
    highest_square_index = len(arr) - 1
    left = 0
    right = len(arr) - 1
    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
        else:
            squares[highest_square_index] = right_square
            right -= 1

        highest_square_index -= 1

    return squares


def main():
    print("Squares: " + str(get_sorted_squares_of_a_sorted_array([-2, -1, 0, 2, 3])))
    print("Squares: " + str(get_sorted_squares_of_a_sorted_array([-3, -1, 0, 1, 2])))

main()
