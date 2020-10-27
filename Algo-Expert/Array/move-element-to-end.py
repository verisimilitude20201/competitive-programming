"""
Solution 1:
----------
1. This is similar to the move-zeroes-to-right.py.
2. We first fill in non 'toMove' elements starting from the 0th index of the array
3. Then, we complete the remaining array with 'toMove' elements.
4. It maintains the order of the non 'moveTo' elements

Complexity:
----------
O(1) Space: In-place modification of the array
O(N) Time: We loop through the array N times.


Solution 2
----------
[2, 1, 2, 2, 2, 2, 3, 4, 2], moveTo = 2


1. Two pointers: i and j

[2, 1, 2, 2, 2, 2, 3, 4, 2]
 i                       j

2. Decrement j till array[j] != moveTo

[2, 1, 2, 2, 2, 2, 3, 4, 2]
 i                    j

3. array[i] == moveTo so swap array[i], array[j]

[4, 1, 2, 2, 2, 2, 3, 2, 2]
 i                    j

4. Increment i

[4, 1, 2, 2, 2, 2, 3, 2, 2]
    i                 j

5. Decrement j till array[j] != moveTo

[4, 1, 2, 2, 2, 2, 3, 2, 2]
    i              j

6. Currently, array[i] is 1 so we cannot swap. Increment i

[4, 1, 2, 2, 2, 2, 3, 2, 2]
       i           j

7. array[i] == moveTo so swap array[i], array[j]

[4, 1, 3, 2, 2, 2, 2, 2, 2]
       i           j

8. Increment i

[4, 1, 3, 2, 2, 2, 2, 2, 2]
          i        j

9. Decrement j till array[j] != moveTo

[4, 1, 3, 2, 2, 2, 2, 2, 2]
       j  i

10. j goes past i, so break out.

[4, 1, 3, 2, 2, 2, 2, 2, 2] 


This does not keep the original order of non 'toMove' elements.

Complexity:
----------
O(1) Space: In-place modification of the array. Although as compared to solution 1, it sets less than N array elements.
O(N) Time: We loop through the array N times.

"""

def moveElementToEnd1(array, toMove):
	idx_non_move_to = 0
	length_of_array = len(array)
	for number in array:
		if number != toMove:
			array[idx_non_move_to] = number
			idx_non_move_to += 1

	while idx_non_move_to < length_of_array:
		array[idx_non_move_to] = toMove
		idx_non_move_to += 1
	
	return array


def moveElementToEnd2(array, toMove):
	i = 0
	j = len(array) - 1
	while i < j:
		while i < j and array[j] == toMove:
			j -= 1

		if array[i] == toMove:
			array[i], array[j] = array[j], array[i]
		i += 1

	return array