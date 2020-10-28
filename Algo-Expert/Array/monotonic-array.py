"""
Concept:
-------
A monotonic function is a function that produces non-increasing or non-decreasing values in mathematics. For example: Square of a positive number is a non-decreasing monotonic function
Here, we need to find out whether an array contains elements that are either non-increasing or non-decreasing in its entirety. Elements can be non-distinct for array.

Solution 1
----------
1. This uses two boolean flags is_non_increasing and is_non_decreasing. It uses elimination. That is the array can either be non-increasing or non-decreasing.
2. If we assume that array is non-increasing
2.1 Each successive element should be smaller than its previous element. A pair that does not satisfy this condition makes the is_non_decreasing flag to false.
3. If we assume that array is non-decreasing
3.1 Each successive element should be greater than its previous element. A pair that does not satisfy this condition makes the is_non_increasing flag to false.
4. After we finish iterating through array, we return is_non_increasing or is_non_decreasing

Solution 2
---------
1. This computes difference between the 0th and first element and maintains a 'direction' variable.
2. Go on computing the differences between each successive elements from index 2 onwards. 
2.1 If direction is 0
2.1.1   Update direction and continue the loop
2.1.2 If direction is less than zero, check if the difference between the previous and current is greater than 0. If so, non-increasing monotonicity is broken
2.1.2 If direction is greater than zero, check if the difference between the previous and current is less than 0. If so, non-decreasing monotonicity is broken 

Complexity
---------
For both algorithms
Time: O(N)
Space: O(1)

"""

def isMonotonic1(array):
	is_non_increasing = True
	is_non_decreasing = True
	for i in range(1, len(array)):
		if array[i] > array[i-1]:
			is_non_decreasing = False
		if array[i] < array[i-1]:
			is_non_increasing = False

	return is_non_increasing or is_non_decreasing




def isMonotonic2(array):
	if len(array) <= 2:
		return True

	direction = array[1] - array[0]
	for i in range(2, len(array)):
		if direction == 0:
			direction = array[i] - array[i-1]
			continue
		if breaksDirection(direction, array[i], array[i-1]):
			return False

	return True

def breaksDirection(direction, current, prev):
	difference = current - prev
	if direction < 0:
		return difference > 0
	return difference < 0