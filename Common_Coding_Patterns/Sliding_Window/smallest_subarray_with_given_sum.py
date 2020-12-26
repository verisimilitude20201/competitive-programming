"""
Problem
-------
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Approach
--------
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

def smallest_subarray_with_given_sum(array, expected_sum):
    min_length = math.inf
    window_start = window_end = 0
    current_sum = 0
    for window_end in range(len(array)):
        current_sum += array[window_end]
        if current_sum >= expected_sum:
            min_length = min(min_length, window_end - window_start + 1)
            current_sum -= array[window_start]
            window_start += 1

    return min_length


print(smallest_subarray_with_given_sum([2, 1, 5, 1, 3, 2], 3))