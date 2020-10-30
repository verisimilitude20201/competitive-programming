"""
Approach
--------
1. Start from index 1
2. Consider each element as peak if and only if its greater than its adjacent elements.
3. Next we measure the length of the peak.
    i. Continue moving left keeping track of positions moved till the numbers are less than the each successive.
    ii. Continue moving to the right of the peak till current number is less than each previous one.
4. Calculate length as right index - left index - 1. 
5. Calculate the max length and return it.


In short,

1. Start at index 1

[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    i

2. A[i - 1] < A[i] and A[i] > A[i+1] condition is false. Just increment i

[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
       i

3. A[i - 1] < A[i] and A[i] > A[i+1] condition is false. Just increment i

[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
          i

4. A[i - 1] < A[i] and A[i] > A[i+1] condition is false. Just increment i

[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
             i

5. A[i - 1] < A[i] and A[i] > A[i+1] condition is true. Initialize leftIdx.

[1, 2, 3,        3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
       leftIdx      i

6. Is A[leftIdx] < A[leftIdx + 1] and leftIdx >= 0? This is false so we break out.

[1, 2, 3,        3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
       leftIdx      i

7. Initialize rightIdx = i + 2
[1, 2, 3, 3, 4, 0, 10,      6, 5, -1, -3, 2, 3]
             i     rightIdx


8. rightIdx < len(array) and A[rightIdx] < A[rightIdx - 1], increment rightIdx. In this case, we break out

9. Increment i

[1, 2, 3, 3, 4, 0, 10,      6, 5, -1, -3, 2, 3]
                i    

10. if A[i - 1] < A[i] and A[i] > A[i] + 1. This is false, so 0 is not a peak

[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
                   i    

11. if A[i - 1] < A[i] and A[i] > A[i] + 1. This is true.


[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
                   i    

12.  Initialize leftIdx


[1, 2, 3, 3, 4,       0, 10, 6, 5, -1, -3, 2, 3]
             leftIdx      i

Complexity:
----------
Space O(1)
Time O(N)

"""
def longestPeak(array):
    i = 1
    longest_peak_length = 0
    while i < len(array) - 1:
    	is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
    	if not is_peak:
    		i += 1
    		continue

    	leftIdx = i - 2
    	while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
    		leftIdx -= 1

    	rightIdx = i + 2
    	while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
    		rightIdx += 1

    	current_peak_length = rightIdx - leftIdx - 1
    	longest_peak_length = max(longest_peak_length, current_peak_length)
    	i = rightIdx

    return longest_peak_length