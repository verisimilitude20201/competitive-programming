"""
Problem
-------
Find the averages of sub-arrays of size K for the given arr and return it.

Approach
-------
Brute Force - Take continuous sum of K elements starting from 0th element, calculate average and return
Fixed length Window of Size K. 

Complexity
---------

Brute Force: 
-----------
    Time: O(N * K) Also performs repeated computation of sum. For example for index 1-5, the sum of elements at index 1 to 4 is already computed
    Space: O(K)

Sliding Window:
-------------
    Time: O(N)
    Space: O(K)

"""
def find_averages_of_subarrays1(K, arr):
    results = []
    for i in range(len(arr)):
        total = 0
        if i + K > len(arr):
            break
        for j in range(i, i + K):
            total += arr[j]
        results.append(round(total / K, 1))

    return results

def find_averages_of_subarrays2(K, arr):
    results = []
    for i in range(len(arr) - K + 1):
        total = 0

        for j in range(i, i + K):
            total += arr[j]
        results.append(round(total / K, 1))

    return results

def find_averages_of_subarrays3(K, arr):
    results = []
    window_start = 0
    total = 0
    for window_end in range(len(arr)):
      total += arr[window_end]
      if window_end >= K - 1:
          results.append(round(total/K, 1))
          total -= arr[window_start]
          window_start += 1

    return results

def main():
    print("Smallest subarray length: " + str(find_averages_of_subarrays1(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])))
    print("Smallest subarray length: " + str(find_averages_of_subarrays1(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])))
    print("Smallest subarray length: " + str(find_averages_of_subarrays3(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])))
    
main()