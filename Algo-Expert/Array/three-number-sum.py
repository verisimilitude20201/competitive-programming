"""
Solution 1: 
-----------
Example: [-8, -6, 1, 2, 3, 5, 6, 12]

Using 3 nested loops to find sum of 3 successive elements in the array. Sorted. 

Complexity
---------
Time: n log(n) + O(n^3) ~ O(n^3)
Space: O(n) 

Solution 2:
------------

1. Sort the array.

[-8, -6, 1, 2, 3, 5, 6, 12]


2.  
    [-8, -6, 1, 2, 3, 5, 6, 12]
    CS   L                  R


3. CS + L + R  
  -8 + -6 + 12 = -2 < 0


4. L = L + 1
   [-8, -6, 1, 2, 3, 5, 6, 12]
    CS      L               R

5. CS + L + R = -8 + 1 + 12 = 5 > 0

6. R = R - 1
[-8, -6, 1, 2, 3, 5, 6, 12]
 CS      L           R

7. CS + L + R = -8 + 1 + 6 = -1 < 0

8. L = L + 1
[-8, -6, 1, 2, 3, 5, 6, 12]
 CS         L        R

9. CS + L + R = -8 + 2 + 6 = 0 - First triplet
   [[-8, 2, 6]]

   and so on.

1. Sort the array.
2. for i in array 
    2.1  Left = i + 1
    2.2. right = len(array) - 1
    2.3  while left < right
    2.3.1   currentSum = array[i] + array[left] + array[right]
    2.3.2   if currentSum = targetSum:
    2.3.2.1     add first triplet; L += 1; R -= 1
    2.3.2.2 elif currentSum < targetSum:
    2.3.2.3     L += 1
    2.3.2.4 elif current > targetSum:
    2.3.2.5     R -= 1

3. Return all triplets

Complexity
---------
Time: O(n^2)
Space: O(n) 

"""
def threeNumberSum1(array, targetSum):
	triplets = []
	array.sort()
	for i in range(len(array) - 2):
		for j in range(i+1, len(array) - 1):
			for k in range(j + 1, len(array)):
				currentSum = array[i] + array[j]  + array[k]
				if currentSum == targetSum:
					triplets.append([array[i], array[j], array[k]])

	return triplets

def threeNumberSum2(array, targetSum):
	array.sort()
	triplets = []
	for i in range(len(array) - 2):
		L = i + 1
		R = len(array) - 1
		while L < R:
			currentSum = array[i] + array[L] + array[R]
			if currentSum == targetSum:
				triplets.append([array[i], array[L], array[R]])
				L = L + 1
				R = R - 1
			elif currentSum < targetSum:
				L += 1
			elif currentSum > targetSum:
				R -= 1

	return triplets

		
			