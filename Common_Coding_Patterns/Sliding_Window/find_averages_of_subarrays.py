"""
Problem: 
-------
Given an array as input, return an array with the averages of all K consecutive elements. 


Approach (Sliding Window Optimized - Constant Window Size):
--------
1.  1 	3 	2 	6 	-1 	4 	1 	8 	2, K = 5     


WindowSum = 0

0  	1	2	3	4	5	6	7	8
1 	3 	2 	6 	-1 	4 	1 	8 	2
WS
WE


2. Jump till K - 1

WindowSum = 11

Result = [2.2, ]

0  	1	2	3	 4	5	6	7	8
1 	3 	2 	6 	-1 	4 	1 	8 	2
__________________
      Sum = 11
WS
				WE


3. Substract the element going out. Substract 1 from Window Sum
	WindowSum = 10 - 1 = 11

4. Compute average

0  	1	2	3	 4	5	6	7	8
1 	3 	2 	6 	-1 	4 	1 	8 	2
    __________________
      Sum = 10    | 4 
    WS
				    WE


  Sum = 14
  Result = [2.2, 2.8]

5. Substract 3 from Sum and move WS ahead. Compute the new sum and average

Sum = 14 - 3 = 11

0  	1	2	3	 4	5	6	7	8
1 	3 	2 	6 	-1 	4 	1 	8 	2
        __________________
         Sum = 11     | 1
    WS
				        WE

    Sum = 12 
    Result = [2.2, 2.8, 2.4]


6. Subtract 2 from sum and move WS ahead. Compute the new sum and average

Sum = 12 - 2 = 10

0  	1	2	3	 4	5	6	7	8
1 	3 	2 	6 	-1 	4 	1 	8 	2
            __________________
             Sum = 10     | 8
            WS
				            WE

Sum = 18
Result = [2.2, 2.8, 2.4, 3.6]


7. Subtract 6 from sum and move WS ahead. Compute the new sum and average

Sum = 18 - 6 = 12

0  	1	2	3	 4	5	6	7	8
1 	3 	2 	6 	-1 	4 	1 	8 	2
                __________________
                 Sum = 12     | 2
                WS
				               WS

Sum = 14

Result = [2.2, 2.8, 2.4, 3.6, 2.8]

Complexity
----------
A. Brute Force

Space: O(K)
Time: O(N * K) where K is the size of the sub-array. 

Disadvantages
-------------
Repeated Calculations at each step along with near quadratic time-complexity

B. Sliding Window Optimized

Space: O(K)
Time: O(N) where K is the size of the sub-array. 

Advantages
-------------
Linear complexity with repeated calculations avoided.

"""

# Brute Force
def find_averages_of_subarrays_brute_force(K, arr):
    averages = [None] * len(arr)
    for i in range(len(arr)):
        total_sum = 0
        for j in range(i, i + K):
            if i + K > len(arr):
                break
            total_sum += arr[j]
        averages[i] = total_sum / K

    return averages


def find_averages_of_subarrays(K, array):
    total_sum = 0
    window_start = 0
    averages = []

    for window_end in range(len(array)):
        total_sum += array[window_end]
        if window_end >= K - 1:
            averages.append(total_sum / K)
            total_sum -= array[window_start]
            window_start += 1

    return averages



# Brute Force
result = find_averages_of_subarrays_brute_force(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Averages of subarrays of size K: " + str(result))

# Optimized 
print(find_averages_of_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))