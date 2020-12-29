"""
Problem
-------
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Approach
--------
Sliding Window - Variable Window Size

[2, 1, 5, 2, 3, 2], Required Sum = 7



1. Initialize WindowsStart and WindowsEnd to 0th element. 

Sum = 0
Min-Length = Infinity

0	1	2	3	4	5
2	1	5	2	3	2
WS
WE

2. Current sum is 2 which is less than 7 the required sum. Increment WE

Sum = 2 

0	1	2	3	4	5
2	1	5	2	3	2
WS
    WE


3. Current sum is 3 which is less than 7 the required sum. Increment WE


0	1	2	3	4	5
2	1	5	2	3	2
WS
        WE

4. Current sum is 8 which is greater than 7 the required sum. Set min-length = WE - WS + 1 = 3. And reduce the size of the window

Sum = 8 - 2 = 6

0	1	2	3	4	5
2	1	5	2	3	2
    WS
        WE

5. Current sum is 6 which is less than 7. Increment WE

0	1	2	3	4	5
2	1	5	2	3	2
    WS
            WE

6. Current sum is again 8 which is greater than 7. No need to set min-length since it's already 2. Reduce the size of window


0	1	2	3	4	5
2	1	5	2	3	2
        WS
            WE

7. Current sum is 7 which is equal to the expected sum 7. Update min-length to WE - WS + 1 = 2. Reduce the size of Window

0	1	2	3	4	5
2	1	5	2	3	2
            WS
            WE

8. 2 is again less than 7 so increment WE

0	1	2	3	4	5
2	1	5	2	3	2
            WS
                WE


9. 5 is less than 7, increment WE

0	1	2	3	4	5
2	1	5	2	3	2
            WS
                    WE

10. Total again equals 7, No need to update min-length now that it's 2. Since WE points to the end of the array exit the loop

Complexity
----------
Time: O(N)
Space: O(1)

"""

import math

def smallest_subarray_with_given_sum(expected_sum, array):
    smallest_subarray_length = math.inf
    window_start = 0
    total_sum = 0
    for window_end in range(len(array)):
        total_sum += array[window_end]
        if total_sum >= expected_sum:
            smallest_subarray_length = min(smallest_subarray_length, window_end - window_start + 1)
            total_sum -= array[window_start]
            window_start += 1

    return smallest_subarray_length


print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))