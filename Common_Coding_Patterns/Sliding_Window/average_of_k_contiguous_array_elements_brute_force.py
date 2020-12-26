"""
Problem: 
-------
Given an array as input, return an array with the averages of all K consecutive elements. 


Complexity
----------
Space: O(K)
Time: O(N * K) where K is the size of the sub-array. 

Disadvantages
-------------
Repeated Calculations at each step along with near quadratic time-complexity

"""

def average_of_k_consecutive_elements(array, K):
    averages = []
    a_sum = 0
    for i in range(len(array)):
        if i + K > len(array):
            break
        a_sum = compute_sum_of_k_contigous_elements(array, i, K)
        averages.append(compute_average(a_sum, K))

    return averages


def compute_sum_of_k_contigous_elements(array, current_iteration, K):
    a_sum = 0
    for j in range(current_iteration, current_iteration + K):
        a_sum += array[j]
    return a_sum


def compute_average(a_sum, K):
    return round(a_sum / K, 2)


print(average_of_k_consecutive_elements([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))


